import traceback
import decimal
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy import select, text
from config.logging_config import logger
from config.config import config
from typing import Any, Dict, List
from sqlalchemy.ext.asyncio import AsyncSession


def convert_decimal(obj: Any) -> Any:
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return obj


def row_to_dict(row) -> Dict[str, Any]:
    # row가 SQLAlchemy 모델 인스턴스가 아닐 경우 dict로 변환하지 않고 그대로 반환
    if not hasattr(row, "__mapper__"):
        return row
    return {
        key: convert_decimal(getattr(row, key))
        for key in row.__mapper__.column_attrs.keys()
    }


async def req_data(
        db: AsyncSession,
        table_info,
        param: str,
        value: str,
):
    try:
        if hasattr(table_info, param):
            stmt = select(table_info).where(getattr(table_info, param) == value)
        else:
            stmt = select(table_info)
        result_data = await db.execute(stmt)
        results = result_data.scalars().all()
        return {"data": [row_to_dict(ret) for ret in results]}
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
        else:
            stmt = text(f"SELECT * FROM {config.sqlalchemy_schema_url}.fn_land_geometry(:pnu)")
            params = {"pnu": value}

        result_data = await db.execute(stmt, params)
        results = result_data.fetchall()

        column_names = result_data.keys()
        response = {
            "data": [
                {''.join([word if i == 0 else word.capitalize() for i, word in enumerate(key.split('_'))]): value
                 for key, value in zip(column_names, row)}
                for row in results
            ]
        }
        return response
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
        stmt_pnu = text(f"SELECT {config.sqlalchemy_schema_url}.fn_pnu_from_address(:address) AS pnu")
        result_pnu = await db.execute(stmt_pnu, {"address": value})
        pnu_row = result_pnu.fetchone()

        if not pnu_row:
            return {"data": []}

        pnu, address = pnu_row[0]

        if table_info:
            stmt = select(table_info).where(table_info.pnu == pnu)
            result_data = await db.execute(stmt)
            results = result_data.scalars().all()
            data = [row_to_dict(ret) for ret in results]
        else:
            data = [{"pnu": pnu, "address": address}]

        return {"data": data}
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

        stmt = select(table_info).where(*filters)
        result_data = await db.execute(stmt, params)
        results = result_data.scalars().all()

        return {"data": [row_to_dict(ret) for ret in results]}
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
