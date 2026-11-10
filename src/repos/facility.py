from src.repos.base import BaseRepository
from src.models.facility import FacilityModel, RoomFacilityModel
from src.schemas.facility import FacilitySchema, RoomFacilitySchema



class FacilityRepository(BaseRepository):
    model = FacilityModel
    schema = FacilitySchema


class RoomFacilityRepository(BaseRepository):
    model = RoomFacilityModel
    schema = RoomFacilitySchema