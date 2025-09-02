import traceback
from fastapi import Depends, APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from database.database import get_db
from database.crud import req_data_realdeal, req_data_realdeal_page
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
    page: int = Query(..., ge=1, description="페이지 번호"),
    size: int = Query(..., ge=1, le=1000, description="페이지당 데이터 개수"),
    pnu: str = Query(..., description="토지고유번호"),
    radius: int = Query(..., ge=1, le=1000, description="반경(미터)"),
    year: str = Query(None, description="연도"),
    db=Depends(get_db),
):
    try:
        result = await req_data_realdeal_page(db, models.TbLandSale, "land-sale", page, size, pnu, radius, year)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 공시지가
@router.get("/land/notice-price", summary="공시지가")
async def land_notice_price(
    pnu: str = Query(..., description="토지고유번호"),
    radius: int = Query(..., ge=1, le=1000, description="반경(미터)"),
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
    page: int = Query(..., ge=1, description="페이지 번호"),
    size: int = Query(..., ge=1, le=10000, description="페이지당 데이터 개수"),
    pnu: str = Query(..., description="토지고유번호"),
    radius: int = Query(..., ge=1, le=1000, description="반경(미터)"),
    year: str = Query(None, description="연도"),
    db=Depends(get_db),
):
    try:
        result = await req_data_realdeal_page(db, models.TbOfficetelRent, "officetel-rent", page, size, pnu, radius, year)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
