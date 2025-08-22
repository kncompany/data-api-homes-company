import traceback
from fastapi import Depends, APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from database.database import get_db
from database.crud import req_data_realdeal
from config.logging_config import logger
from database import models

API_MAIN_TITLE = "[빅밸류]"
API_TITLE = "홈즈 컴퍼니 실거래"

router = APIRouter(
    prefix="",
    tags=[f"{API_MAIN_TITLE} {API_TITLE}"],
)


# 토지매매실거래
@router.get("/realdeal/land-sale", summary="토지매매실거래")
async def realdeal_land_sale(
    pnu: str = Query(..., description="토지고유번호"),
    radius: str = Query(..., description="반경(미터)"),
    year: str = Query(None, description="연도"),
    db=Depends(get_db),
):
    try:
        result = await req_data_realdeal(db, models.TbLandSale, "land-sale", pnu, radius, year)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 공시지가
@router.get("/land/notice-price", summary="공시지가")
async def land_notice_price(
    pnu: str = Query(..., description="토지고유번호"),
    radius: str = Query(..., description="반경(미터)"),
    year: str = Query(None, description="연도"),
    db=Depends(get_db),
):
    try:
        result = await req_data_realdeal(db, models.TbLandNoticePrice, "notice-price", pnu, radius, year)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 오피스텔임대실거래
@router.get("/realdeal/officetel-rent", summary="오피스텔임대실거래")
async def realdeal_officetel_rent(
    pnu: str = Query(..., description="토지고유번호"),
    radius: str = Query(..., description="반경(미터)"),
    year: str = Query(None, description="연도"),
    db=Depends(get_db),
):
    try:
        result = await req_data_realdeal(db, models.TbOfficetelRent, "officetel-rent", pnu, radius, year)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
