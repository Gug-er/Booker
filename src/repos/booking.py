from src.repos.base import BaseRepository
from src.models.booking import BookingModel
from src.repos.mappers.booking import BookingDataMapper



class BookingRepository(BaseRepository):
    model = BookingModel
    mapper = BookingDataMapper