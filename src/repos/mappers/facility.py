from src.repos.mappers.base import DataMapper
from src.models.facility import FacilityModel
from src.models.facility import RoomFacilityModel
from src.schemas.facility import FacilitySchema
from src.schemas.facility import RoomFacilitySchema



class FacilityDataMapper(DataMapper):
    db_model = FacilityModel
    schema = FacilitySchema


class RoomFacilityDataMapper(DataMapper):
    db_model = RoomFacilityModel
    schema = RoomFacilitySchema