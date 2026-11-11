from src.repos.mappers.base import DataMapper
from src.models.hotel import HotelModel
from src.schemas.hotel import HotelSchema



class HotelDataMapper(DataMapper):
    db_model = HotelModel
    schema = HotelSchema