from src.repos.base import BaseRepository
from src.models.booking import BookingModel
from src.schemas.booking import BookingSchema

class BookingRepository(BaseRepository):
    model = BookingModel
    schema = BookingSchema