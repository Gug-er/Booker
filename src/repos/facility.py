from src.repos.base import BaseRepository
from src.models.facility import FacilityModel
from src.schemas.facility import FacilitySchema, FacilityAdd



class FacilityRepository(BaseRepository):
    model = FacilityModel
    schema = FacilitySchema