import traceback
import decimal
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, text
from config.logging_config import logger
from config.config import config
from typing import Any, Dict, List
from sqlalchemy.ext.asyncio import AsyncSession


def to_camel_case(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


async def req_data(
        db: AsyncSession,
        table_info,
        param: str,
        value: str,
):
    try:
        stmt = text(
            f"SELECT * FROM {config.sqlalchemy_schema_url}.{table_info.__tablename__} WHERE {param} = :value")
        params = {"value": value}
        result_data = await db.execute(stmt, params)
        results = result_data.fetchall()
        data = [
            {to_camel_case(key): val for key, val in dict(row._mapping).items()}
            for row in results
        ]
        if not data:
            # 만약 fetchall 결과가 없고 scalars().all()로 모델 인스턴스가 반환된다면
            result_data = await db.execute(select(table_info))
            results = result_data.scalars().all()
            data = [
                {to_camel_case(key): value for key, value in obj.__dict__.items() if not key.startswith('_')}
                for obj in results
            ]
        return {"data": jsonable_encoder(data)}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


async def req_data_pnu(
        db: AsyncSession,
        table_info,
        param: str,
        value: str,
):
    try:
        if param == "address":
            stmt = text(
                f"with step1 as (select pnu from {config.sqlalchemy_schema_url}.fn_pnu_from_address(:address)) "
                f"select b.* from step1 as a cross join lateral {config.sqlalchemy_schema_url}.fn_land_geometry(a.pnu) as b"
            )
            params = {"address": value}
            result_data = await db.execute(stmt, params)
            results = result_data.fetchall()
            data = [
                {to_camel_case(key): val for key, val in dict(row._mapping).items()}
                for row in results
            ]
        else:
            stmt = text(f"SELECT * FROM {config.sqlalchemy_schema_url}.fn_land_geometry(:pnu)")
            params = {"pnu": value}
            result_data = await db.execute(stmt, params)
            results = result_data.fetchall()
            data = [
                {to_camel_case(key): val for key, val in dict(row._mapping).items()}
                for row in results
            ]

        return {"data": jsonable_encoder(data)}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


async def req_data_address(
        db: AsyncSession,
        table_info,
        param: str,
        value: str,
):
    try:
        if table_info:
            stmt = text(
                f"SELECT a.* "
                f"FROM {config.sqlalchemy_schema_url}.{table_info.__tablename__} as a "
                f"CROSS JOIN LATERAL {config.sqlalchemy_schema_url}.fn_pnu_from_address(:address) as b "
                f"WHERE a.pnu = b.pnu"
            )
            result_data = await db.execute(stmt, {"address": value})
            results = result_data.fetchall()
            data = [
                {to_camel_case(key): val for key, val in dict(row._mapping).items()}
                for row in results
            ]
        else:
            stmt_pnu = text(f"SELECT {config.sqlalchemy_schema_url}.fn_pnu_from_address(:address) AS pnu")
            result_pnu = await db.execute(stmt_pnu, {"address": value})
            pnu_rows = result_pnu.fetchall()
            data = []
            for pnu_row in pnu_rows:
                pnu_result = pnu_row[0]
                if isinstance(pnu_result, tuple):
                    pnu = pnu_result[0]
                    address = pnu_result[1] if len(pnu_result) > 1 else value
                else:
                    pnu = pnu_result
                    address = value
                data.append({"pnu": pnu, "landNumberAddress": address})

        return {"data": jsonable_encoder(data)}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


async def req_data_realdeal(
        db: AsyncSession,
        table_info,
        gubun: str,
        pnu: str,
        radius: str,
        year: str,
):
    try:
        # 테이블명 결정
        table_name = table_info.__tablename__
        schema = config.sqlalchemy_schema_url
        # 쿼리 조건 분기
        if gubun == "land-sale":
            year_cond = f"WHERE a.contract_date LIKE '{year}%'" if year else ""
        elif gubun == "notice-price":
            year_cond = f"WHERE a.notice_standard_year = '{year}'" if year else ""
        elif gubun == "officetel-rent":
            year_cond = f"WHERE a.contract_date LIKE '{year}%'" if year else ""
        else:
            year_cond = ""
        # 쿼리 생성
        query = (
            f"WITH step1 AS (SELECT pnu FROM {schema}.fn_get_near_pnu(:pnu, :radius)) "
            f"SELECT a.* FROM {schema}.{table_name} AS a "
            f"INNER JOIN step1 AS b ON a.pnu = b.pnu "
            f"{year_cond}"
        )
        params = {"pnu": pnu, "radius": int(radius)}
        result_data = await db.execute(text(query), params)
        results = result_data.fetchall()
        data = [
            {to_camel_case(key): val for key, val in dict(row._mapping).items()}
            for row in results
        ]
        return {"data": jsonable_encoder(data)}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
