from src.repos.base import BaseRepository
from src.models.room import RoomModel
from src.schemas.room import RoomSchema



class RoomRepository(BaseRepository):
    model = RoomModel
    schema = RoomSchema