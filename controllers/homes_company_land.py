import traceback
from fastapi import Depends, APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from database.database import get_db
from database.crud import req_data, req_data_address, req_data_pnu
from config.logging_config import logger
from database import models

API_MAIN_TITLE = "[빅밸류]"
API_TITLE = "홈즈 컴퍼니 토지정보"

router = APIRouter(
    prefix="",
    tags=[f"{API_MAIN_TITLE} {API_TITLE}"],
)


# 토지특성 지번주소
@router.get("/land/feature/address", summary="토지특성 지번주소")
async def land_feature_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbLandFeature, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 토지특성 토지고유번호
@router.get("/land/feature/pnu", summary="토지특성 토지고유번호")
async def land_feature_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbLandFeature, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# pnu변환 지번주소
@router.get("/land/pnu/address", summary="pnu변환 지번주소")
async def land_pnu_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, None, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 토지이용계획 지번주소
@router.get("/land/use/address", summary="토지이용계획 지번주소")
async def land_use_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbLandUse, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 토지이용계획 토지고유번호
@router.get("/land/use/pnu", summary="토지이용계획 토지고유번호")
async def land_use_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbLandUse, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 지적도형 지번주소
@router.get("/land/geometry/address", summary="지적도형 지번주소")
async def land_geometry_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_pnu(db, models.TbLandGeometry, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 지적도형 토지고유번호
@router.get("/land/geometry/pnu", summary="지적도형 토지고유번호")
async def land_geometry_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data_pnu(db, models.TbLandGeometry, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
