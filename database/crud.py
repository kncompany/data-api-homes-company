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
        near_pnu_cte = text(f"SELECT pnu FROM {config.sqlalchemy_schema_url}.fn_get_near_pnu(:pnu, :radius)")
        params = {"pnu": pnu, "radius": int(radius)}
        filters = [
            table_info.pnu.in_(
                select(text("pnu")).select_from(text(f"({near_pnu_cte}) AS near_pnu"))
            )
        ]

        if year:
            if gubun in ["land-sale", "officetel-rent"]:
                filters.append(table_info.contractDate.like(f"{year}%"))
            elif gubun == "notice-price":
                filters.append(table_info.noticeStandardYear == year)

        stmt = select(table_info).where(*filters).distinct()
        result_data = await db.execute(stmt, params)
        results = result_data.scalars().all()
        
        # 중복 제거를 위한 집합 사용
        seen_records = set()
        unique_data = []
        
        for obj in results:
            # 고유 식별자 생성 (모든 필드 값의 해시)
            record_dict = {to_camel_case(key): value for key, value in obj.__dict__.items() if not key.startswith('_')}
            record_key = str(sorted(record_dict.items()))
            
            if record_key not in seen_records:
                seen_records.add(record_key)
                unique_data.append(record_dict)
        
        return {"data": jsonable_encoder(unique_data)}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
