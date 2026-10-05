from src.repos.base import BaseRepository
from src.models.room import RoomModel


class RoomRepository(BaseRepository):
    model = RoomModel