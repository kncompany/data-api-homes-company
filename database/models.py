from sqlalchemy import Column, String, CHAR, Numeric
from sqlalchemy.ext.declarative import declarative_base
from config.config import config


BaseTable = declarative_base()
BaseTable.metadata.schema = config.sqlalchemy_schema_url


# 표제부
class TbTitlePart(BaseTable):
    __tablename__ = "tb_title_part"
    pnu = Column("pnu", CHAR(19))
    ppk = Column("ppk", String(33), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    buildingDivisionCode = Column("building_division_code", String(1))
    buildingDivisionName = Column("building_division_name", String(100))
    documentDivisionCode = Column("document_division_code", String(1))
    documentDivisionName = Column("document_division_name", String(100))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    outsideLandNumberCount = Column("outside_land_number_count", Numeric(5))
    roadCode = Column("road_code", String(12))
    eupmyeondongSeriesCode = Column("eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    dongName = Column("dong_name", String(100))
    mainSubDivisionCode = Column("main_sub_division_code", String)
    mainSubDivisionName = Column("main_sub_division_name", String(100))
    landArea = Column("land_area", Numeric(19, 9))
    buildingArea = Column("building_area", Numeric(19, 9))
    buildingcoverageRate = Column("buildingcoverage_rate", Numeric(19, 9))
    totalFloorArea = Column("total_floor_area", Numeric(19, 9))
    floorareaRateCalculationPurposeTotalFloorArea = Column("floorarea_rate_calculation_purpose_total_floor_area", Numeric(19, 9))
    floorareaRate = Column("floorarea_rate", Numeric(19, 9))
    structureCode = Column("structure_code", String(2))
    structureName = Column("structure_name", String(100))
    etcStructureName = Column("etc_structure_name", String(500))
    purposeCode = Column("purpose_code", String(5))
    purposeName = Column("purpose_name", String(100))
    etcPurposeName = Column("etc_purpose_name", String(500))
    roofCode = Column("roof_code", String(2))
    roofName = Column("roof_name", String(100))
    etcRoofName = Column("etc_roof_name", String(500))
    householdCount = Column("household_count", Numeric(5))
    familyCount = Column("family_count", Numeric(5))
    height = Column("height", Numeric(19, 9))
    groundFloorCount = Column("ground_floor_count", Numeric(5))
    undergroundFloorCount = Column("underground_floor_count", Numeric(5))
    passengerElevatorCount = Column("passenger_elevator_count", Numeric(5))
    emergencyElevatorCount = Column("emergency_elevator_count", Numeric(5))
    subBuildingCount = Column("sub_building_count", Numeric(5))
    subBuildingArea = Column("sub_building_area", Numeric(19, 9))
    totalTotalFloorArea = Column("total_total_floor_area", Numeric(19, 9))
    indoorMechanicalParkingCount = Column("indoor_mechanical_parking_count", Numeric(6))
    indoorMechanicalParkingArea = Column("indoor_mechanical_parking_area", Numeric(19, 9))
    outdoorMechanicalParkingCount = Column("outdoor_mechanical_parking_count", Numeric(6))
    outdoorMechanicalParkingArea = Column("outdoor_mechanical_parking_area", Numeric(19, 9))
    indoorDirectParkingCount = Column("indoor_direct_parking_count", Numeric(6))
    indoorDirectParkingArea = Column("indoor_direct_parking_area", Numeric(19, 9))
    outdoorDirectParkingCount = Column("outdoor_direct_parking_count", Numeric(6))
    outdoorDirectParkingArea = Column("outdoor_direct_parking_area", Numeric(19, 9))
    permissionDate = Column("permission_date", String(8))
    constructionStartDate = Column("construction_start_date", String(8))
    useApprovalDate = Column("use_approval_date", String(8))
    permissionNumberYear = Column("permission_number_year", String(4))
    permissionNumberAgencyCode = Column("permission_number_agency_code", CHAR(7))
    permissionNumberAgencyName = Column("permission_number_agency_name", String(100))
    permissionNumberDivisionCode = Column("permission_number_division_code", String(4))
    permissionNumberDivisionName = Column("permission_number_division_name", String(100))
    hoCount = Column("ho_count", Numeric(5))
    energyEfficiencyGrade = Column("energy_efficiency_grade", String(4))
    energySavingRate = Column("energy_saving_rate", Numeric(19, 9))
    energyEpiScore = Column("energy_epi_score", Numeric(5))
    ecoBuildingGrade = Column("eco_building_grade", String)
    ecoBuildingCertificationScore = Column("eco_building_certification_score", Numeric(5))
    intelligentBuildingGrade = Column("intelligent_building_grade", String)
    intelligentBuildingCertificationScore = Column("intelligent_building_certification_score", Numeric(5))
    createDate = Column("create_date", String(8))
    quakeproofDesignIs = Column("quakeproof_design_is", String(1))
    quakeproofDesignGrade = Column("quakeproof_design_grade", String(200))
    class Config:
        orm_mode = True


# 부속지번
class TbSubLandNumber(BaseTable):
    __tablename__ = "tb_sub_land_number"
    pnu = Column("pnu", CHAR(19))
    subPnu = Column("sub_pnu", CHAR(19), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    buildingDocumentManagementNumber = Column("building_document_management_number", String(33), primary_key=True)
    buildingDivisionCode = Column("building_division_code", String(1))
    buildingDivisionName = Column("building_division_name", String(100))
    documentDivisionCode = Column("document_division_code", String(1))
    documentDivisionName = Column("document_division_name", String(100))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sigunguCode = Column("sigungu_code", String(5))
    legalEupmyeondongRiCode = Column("legal_eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    sigunguRoadCode = Column("sigungu_road_code", String(12))
    legalEupmyeondongSeriesCode = Column("legal_eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    subBuildingDivisionCode = Column("sub_building_division_code", String)
    subBuildingDivisionName = Column("sub_building_division_name", String(100))
    subSigunguCode = Column("sub_sigungu_code", String(5))
    subLegalEupmyeondongRiCode = Column("sub_legal_eupmyeondong_ri_code", String(5))
    subLandNumberDivisionCode = Column("sub_land_number_division_code", String(2))
    subMainLandNumber = Column("sub_main_land_number", String(4))
    subSubLandNumber = Column("sub_sub_land_number", String(4))
    subSpecialLandName = Column("sub_special_land_name", String(200))
    subBlockName = Column("sub_block_name", String(20))
    subLotName = Column("sub_lot_name", String(20))
    subEtcLandNumberName = Column("sub_etc_land_number_name", String(300))
    createDate = Column("create_date", String(8))

    class Config:
        orm_mode = True


# 총괄표제부
class TbAggregateTitlePart(BaseTable):
    __tablename__ = "tb_aggregate_title_part"

    pnu = Column("pnu", CHAR(19))
    gppk = Column("gppk", String(33), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    buildingDivisionCode = Column("building_division_code", String(1))
    buildingDivisionName = Column("building_division_name", String(100))
    documentDivisionCode = Column("document_division_code", String(1))
    documentDivisionName = Column("document_division_name", String(100))
    newOldDocumentDivisionCode = Column("new_old_document_division_code", String(1))
    newOldDocumentDivisionName = Column("new_old_document_division_name", String(100))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    outsideLandNumberCount = Column("outside_land_number_count", Numeric(5))
    roadCode = Column("road_code", String(12))
    eupmyeondongSeriesCode = Column("eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    landArea = Column("land_area", Numeric(19, 9))
    buildingArea = Column("building_area", Numeric(19, 9))
    buildingcoverageRate = Column("buildingcoverage_rate", Numeric(19, 9))
    totalFloorArea = Column("total_floor_area", Numeric(19, 9))
    floorareaRateCalculationPurposeTotalFloorArea = Column("floorarea_rate_calculation_purpose_total_floor_area", Numeric(19, 9))
    floorareaRate = Column("floorarea_rate", Numeric(19, 9))
    purposeCode = Column("purpose_code", String(5))
    purposeName = Column("purpose_name", String(100))
    etcPurposeName = Column("etc_purpose_name", String(500))
    householdCount = Column("household_count", Numeric(5))
    familyCount = Column("family_count", Numeric(5))
    mainBuildingCount = Column("main_building_count", Numeric(5))
    subBuildingCount = Column("sub_building_count", Numeric(5))
    subBuildingArea = Column("sub_building_area", Numeric(19, 9))
    totalParkingCount = Column("total_parking_count", Numeric(7))
    indoorMechanicalParkingCount = Column("indoor_mechanical_parking_count", Numeric(6))
    indoorMechanicalParkingArea = Column("indoor_mechanical_parking_area", Numeric(19, 9))
    outdoorMechanicalParkingCount = Column("outdoor_mechanical_parking_count", Numeric(6))
    outdoorMechanicalParkingArea = Column("outdoor_mechanical_parking_area", Numeric(19, 9))
    indoorDirectParkingCount = Column("indoor_direct_parking_count", Numeric(6))
    indoorDirectParkingArea = Column("indoor_direct_parking_area", Numeric(19, 9))
    outdoorDirectParkingCount = Column("outdoor_direct_parking_count", Numeric(6))
    outdoorDirectParkingArea = Column("outdoor_direct_parking_area", Numeric(19, 9))
    permissionDate = Column("permission_date", String(8))
    constructionStartDate = Column("construction_start_date", String(8))
    useApprovalDate = Column("use_approval_date", String(8))
    permissionNumberYear = Column("permission_number_year", String(4))
    permissionNumberAgencyCode = Column("permission_number_agency_code", CHAR(7))
    permissionNumberAgencyName = Column("permission_number_agency_name", String(100))
    permissionNumberDivisionCode = Column("permission_number_division_code", String(4))
    permissionNumberDivisionName = Column("permission_number_division_name", String(100))
    hoCount = Column("ho_count", Numeric(5))
    energyEfficiencyGrade = Column("energy_efficiency_grade", String(4))
    energySavingRate = Column("energy_saving_rate", Numeric(19, 9))
    energyEpiScore = Column("energy_epi_score", Numeric(5))
    ecoBuildingGrade = Column("eco_building_grade", CHAR(1))
    ecoBuildingCertificationScore = Column("eco_building_certification_score", Numeric(5))
    intelligentBuildingGrade = Column("intelligent_building_grade", CHAR(1))
    intelligentBuildingCertificationScore = Column("intelligent_building_certification_score", Numeric(5))
    createDate = Column("create_date", String(8))

    class Config:
        orm_mode = True


# 층별개요
class TbFloorOverview(BaseTable):
    __tablename__ = "tb_floor_overview"
    pnu = Column("pnu", CHAR(19))
    ppk = Column("ppk", String(33), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    roadCode = Column("road_code", String(12))
    eupmyeondongSeriesCode = Column("eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    dongName = Column("dong_name", String(100))
    floorDivisionCode = Column("floor_division_code", String(2))
    floorDivisionName = Column("floor_division_name", String(100))
    floorNumber = Column("floor_number", Numeric(4))
    floorName = Column("floor_name", String(100))
    structureCode = Column("structure_code", String(2))
    structureName = Column("structure_name", String(100))
    etcStructureName = Column("etc_structure_name", String(500))
    purposeCode = Column("purpose_code", String(5))
    purposeName = Column("purpose_name", String(100))
    etcPurposeName = Column("etc_purpose_name", String(500))
    area = Column("area", Numeric(19, 9))
    mainSubDivisionCode = Column("main_sub_division_code", String(1))
    mainSubDivisionName = Column("main_sub_division_name", String(100))
    areaExceptIs = Column("area_except_is", String(1))
    createDate = Column("create_date", String(8))

    class Config:
        orm_mode = True


# 기본개요
class TbBasicOverview(BaseTable):
    __tablename__ = "tb_basic_overview"
    pnu = Column("pnu", CHAR(19))
    buildingDocumentManagementNumber = Column("building_document_management_number", String(33), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    buildingDocumentUpperManagementNumber = Column("building_document_upper_management_number", String(33))
    buildingDivisionCode = Column("building_division_code", String(1))
    buildingDivisionName = Column("building_division_name", String(100))
    documentDivisionCode = Column("document_division_code", String(1))
    documentDivisionName = Column("document_division_name", String(100))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    outsideLandNumberCount = Column("outside_land_number_count", Numeric(5))
    roadCode = Column("road_code", String(12))
    eupmyeondongSeriesCode = Column("eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    purposeRegionCode = Column("purpose_region_code", String(6))
    purposeDistrictCode = Column("purpose_district_code", String(6))
    purposeZoneCode = Column("purpose_zone_code", String(6))
    purposeRegionName = Column("purpose_region_name", String(100))
    purposeDistrictName = Column("purpose_district_name", String(100))
    purposeZoneName = Column("purpose_zone_name", String(100))
    createDate = Column("create_date", String(8))

    class Config:
        orm_mode = True


# 전유부
class TbPrivatePart(BaseTable):
    __tablename__ = "tb_private_part"
    pnu = Column("pnu", CHAR(19))
    ppk = Column("ppk", String(33))
    jpk = Column("jpk", String(33), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    buildingDivisionCode = Column("building_division_code", String(1))
    buildingDivisionName = Column("building_division_name", String(100))
    documentDivisionCode = Column("document_division_code", String(1))
    documentDivisionName = Column("document_division_name", String(100))
    landNumberAddress = Column("land_number_address", String(500))
    roadNameAddress = Column("road_name_address", String(400))
    buildingName = Column("building_name", String(100))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    landNumberDivisionCode = Column("land_number_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    specialLandName = Column("special_land_name", String(200))
    blockName = Column("block_name", String(20))
    lotName = Column("lot_name", String(20))
    roadCode = Column("road_code", String(12))
    eupmyeondongSeriesCode = Column("eupmyeondong_series_code", String(5))
    undergroundDivisionCode = Column("underground_division_code", String(1))
    mainBuildingNumber = Column("main_building_number", Numeric(5))
    subBuildingNumber = Column("sub_building_number", Numeric(5))
    dongName = Column("dong_name", String(100))
    hoName = Column("ho_name", String(100))
    floorDivisionCode = Column("floor_division_code", String(2))
    floorDivisionName = Column("floor_division_name", String(100))
    floorNumber = Column("floor_number", Numeric(4))
    createDate = Column("create_date", String(8))
    class Config:
        orm_mode = True


# 토지특성
class TbLandFeature(BaseTable):
    __tablename__ = "tb_land_feature"
    noticeStandardYear = Column("notice_standard_year", CHAR(4))
    noticeStandardMonth = Column("notice_standard_month", CHAR(2))
    pnu = Column("pnu", CHAR(19), primary_key=True)
    landNumber = Column("land_number", CHAR(9))
    landSeriesNumber = Column("land_series_number", String(6))
    landPurposeCode = Column("land_purpose_code", CHAR(2))
    landArea = Column("land_area", Numeric(17, 5))
    purposeRegionDivision1Code = Column("purpose_region_division_1_code", CHAR(2))
    purposeRegionDivision2Code = Column("purpose_region_division_2_code", CHAR(2))
    landUseSituationCode = Column("land_use_situation_code", CHAR(5))
    landHeightCode = Column("land_height_code", CHAR(2))
    landShapeCode = Column("land_shape_code", CHAR(2))
    roadBoundaryCode = Column("road_boundary_code", CHAR(2))
    individualNoticeLandPrice = Column("individual_notice_land_price", Numeric(12))
    landPurposeName = Column("land_purpose_name", String(100))
    purposeRegionDivision1Name = Column("purpose_region_division_1_name", String(100))
    purposeRegionDivision2Name = Column("purpose_region_division_2_name", String(100))
    landUseSituationName = Column("land_use_situation_name", String(100))
    landHeightName = Column("land_height_name", String(100))
    landShapeName = Column("land_shape_name", String(100))
    roadBoundaryName = Column("road_boundary_name", String(100))

    class Config:
        orm_mode = True


# 토지이요계획
class TbLandUse(BaseTable):
    __tablename__ = "tb_land_use"
    pnu = Column("pnu", CHAR(19), primary_key=True)
    standardYm = Column("standard_ym", CHAR(6))
    sidoSigunguCode = Column("sido_sigungu_code", String(5))
    eupmyeondongRiCode = Column("eupmyeondong_ri_code", String(5))
    documentDivisionCode = Column("document_division_code", String(1))
    mainLandNumber = Column("main_land_number", String(4))
    subLandNumber = Column("sub_land_number", String(4))
    mapNumber = Column("map_number", String(40), primary_key=True)
    violationDivisionCode = Column("violation_division_code", String(2), primary_key=True)
    purposeRegionDistrictZoneCode = Column("purpose_region_district_zone_code", String(30))
    conversionDivisionCode = Column("conversion_division_code", String(2))
    approvalIs = Column("approval_is", String(2))
    approvalDate = Column("approval_date", String(30))
    referenceContent = Column("reference_content", String(500))
    insertDatetime = Column("insert_datetime", String(20))
    sourceSidoSigunguCode = Column("source_sido_sigungu_code", String(5))
    violationDivisionName = Column("violation_division_name", String(100))
    purposeRegionDistrictZoneName = Column("purpose_region_district_zone_name", String(100))

    class Config:
        orm_mode = True


# 지적도형
class TbLandGeometry(BaseTable):
    __tablename__ = "tb_land_geometry"
    standardYm = Column("standard_ym", CHAR(6))
    pnu = Column("pnu", CHAR(19), primary_key=True)
    geometry = Column("geometry")  # 실제 geometry 타입은 DB에서 관리

    class Config:
        orm_mode = True


# 토지매매실거래
class TbLandSale(BaseTable):
    __tablename__ = "tb_land_sale"
    pnu = Column("pnu", CHAR(19), primary_key=True)
    landNumberAddress = Column("land_number_address", String(500))
    landPurposeName = Column("land_purpose_name", String(50))
    purposeRegionName = Column("purpose_region_name", String(50))
    buildingMainPurposeName = Column("building_main_purpose_name", String(50))
    roadConditionName = Column("road_condition_name", String(50))
    contractArea = Column("contract_area", Numeric(19, 9))
    price = Column("price", Numeric(13))
    contractDate = Column("contract_date", String(8))
    shareDivisionName = Column("share_division_name", String(50))
    cancelDate = Column("cancel_date", String(20))
    dealTypeName = Column("deal_type_name", String(50))
    brokerAddress = Column("broker_address", String(500))

    class Config:
        orm_mode = True


# 공시지가
class TbLandNoticePrice(BaseTable):
    __tablename__ = "tb_land_notice_price"
    pnu = Column("pnu", CHAR(19), primary_key=True)
    noticeStandardYear = Column("notice_standard_year", String(4), primary_key=True)
    noticeStandardMonth = Column("notice_standard_month", String(2), primary_key=True)
    noticePrice = Column("notice_price", Numeric(13))

    class Config:
        orm_mode = True


# 오피스텔임대실거래
class TbOfficetelRent(BaseTable):
    __tablename__ = "tb_officetel_rent"
    pnu = Column("pnu", CHAR(19), primary_key=True)
    legaldongName = Column("legaldong_name", String(100))
    landNumber = Column("land_number", String(20))
    complexName = Column("complex_name", String(50))
    dealDivisionName = Column("deal_division_name", String(10))
    privateArea = Column("private_area", Numeric(13, 4))
    contractDate = Column("contract_date", CHAR(8))
    depositPrice = Column("deposit_price", Numeric(13))
    price = Column("price", Numeric(13))
    floorName = Column("floor_name", String(10))
    constructionYear = Column("construction_year", CHAR(4))
    contractStartYm = Column("contract_start_ym", CHAR(6))
    contractEndYm = Column("contract_end_ym", CHAR(6))
    contractDivisionName = Column("contract_division_name", String(2))
    renewalRequestIs = Column("renewal_request_is", String(2))
    oldDepositPrice = Column("old_deposit_price", Numeric(13))
    oldPrice = Column("old_price", Numeric(13))
    class Config:
        orm_mode = True
