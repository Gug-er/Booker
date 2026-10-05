from src.repos.base import BaseRepository
from src.models.hotel import HotelModel
from src.schemas.hotel import HotelSchema

class HotelRepository(BaseRepository):
    model = HotelModel
    schema = HotelSchema