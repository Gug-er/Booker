from src.repos.mappers.base import DataMapper
from src.models.booking import BookingModel
from src.schemas.booking import BookingSchema



class BookingDataMapper(DataMapper):
    db_model = BookingModel
    schema = BookingSchema