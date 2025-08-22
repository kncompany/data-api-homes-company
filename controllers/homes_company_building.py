import traceback
from fastapi import Depends, APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from database.database import get_db
from database.crud import req_data, req_data_address
from config.logging_config import logger
from database import models

API_MAIN_TITLE = "[빅밸류]"
API_TITLE = "홈즈 컴퍼니 건축물대장"

router = APIRouter(
    prefix="",
    tags=[f"{API_MAIN_TITLE} {API_TITLE}"],
)


# 표제부 지번주소
@router.get("/building-document/title-part/address", summary="표제부 지번주소")
async def building_document_title_part_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbTitlePart, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 표제부 토지고유번호
@router.get("/building-document/title-part/pnu", summary="표제부 토지고유번호")
async def building_document_title_part_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbTitlePart, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 표제부 표제건물대장관리번호
@router.get("/building-document/title-part/ppk", summary="표제부 표제건물대장관리번호")
async def building_document_title_part_ppk(
    value: str = Query(..., description="표제건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbTitlePart, "ppk", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 부속지번 지번주소
@router.get("/building-document/sub-land-number/address", summary="부속지번 지번주소")
async def building_document_sub_land_number_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbSubLandNumber,  "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 부속지번 토지고유번호
@router.get("/building-document/sub-land-number/pnu", summary="부속지번 토지고유번호")
async def building_document_sub_land_number_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbSubLandNumber, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 부속지번 건물대장관리번호
@router.get("/building-document/sub-land-number/building_document_management_number", summary="부속지번 건물대장관리번호")
async def building_document_sub_land_number_management_number(
    value: str = Query(..., description="건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbSubLandNumber, "building_document_management_number", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 부속지번 부속토지고유번호
@router.get("/building-document/sub-land-number/sub_pnu", summary="부속지번 부속토지고유번호")
async def building_document_sub_land_number_sub_pnu(
    value: str = Query(..., description="부속토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbSubLandNumber, "sub_pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 총괄표제부 지번주소
@router.get("/building-document/aggregate-title-part/address", summary="총괄표제부 지번주소")
async def building_document_aggregate_title_part_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbAggregateTitlePart, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 총괄표제부 토지고유번호
@router.get("/building-document/aggregate-title-part/pnu", summary="총괄표제부 토지고유번호")
async def building_document_aggregate_title_part_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbAggregateTitlePart, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 총괄표제부 총괄표제건물대장관리번호
@router.get("/building-document/aggregate-title-part/gppk", summary="총괄표제부 총괄표제건물대장관리번호")
async def building_document_aggregate_title_part_gppk(
    value: str = Query(..., description="총괄표제건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbAggregateTitlePart, "gppk", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 층별개요 지번주소
@router.get("/building-document/floor-overview/address", summary="층별개요 지번주소")
async def building_document_floor_overview_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbFloorOverview, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 층별개요 토지고유번호
@router.get("/building-document/floor-overview/pnu", summary="층별개요 토지고유번호")
async def building_document_floor_overview_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbFloorOverview, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 층별개요 표제건물대장관리번호
@router.get("/building-document/floor-overview/ppk", summary="층별개요 표제건물대장관리번호")
async def building_document_floor_overview_ppk(
    value: str = Query(..., description="표제건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbFloorOverview, "ppk", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 기본개요 건물대장상위관리번호
@router.get("/building-document/basic-overview/building_document_upper_management_number", summary="기본개요 건물대장상위관리번호")
async def building_document_basic_overview_upper_management_number(
    value: str = Query(..., description="건물대장상위관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbBasicOverview, "building_document_upper_management_number", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 전유부 지번주소
@router.get("/building-document/private-part/address", summary="전유부 지번주소")
async def building_document_private_part_address(
    value: str = Query(..., description="지번주소"),
    db=Depends(get_db),
):
    try:
        result = await req_data_address(db, models.TbPrivatePart, "address", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 전유부 토지고유번호
@router.get("/building-document/private-part/pnu", summary="전유부 토지고유번호")
async def building_document_private_part_pnu(
    value: str = Query(..., description="토지고유번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbPrivatePart, "pnu", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 전유부 전유건물대장관리번호
@router.get("/building-document/private-part/jpk", summary="전유부 전유건물대장관리번호")
async def building_document_private_part_jpk(
    value: str = Query(..., description="전유건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbPrivatePart, "jpk", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])


# 전유부 표제건물대장관리번호
@router.get("/building-document/private-part/ppk", summary="전유부 표제건물대장관리번호")
async def building_document_private_part_ppk(
    value: str = Query(..., description="표제건물대장관리번호"),
    db=Depends(get_db),
):
    try:
        result = await req_data(db, models.TbPrivatePart, "ppk", value)
        return ORJSONResponse(result)
    except Exception as e:
        logger.error(f"Exception error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=[{"msg": str(e)}])
