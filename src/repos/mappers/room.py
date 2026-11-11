from src.repos.mappers.base import DataMapper
from src.models.room import RoomModel
from src.schemas.room import RoomSchema, RoomWithRels



class RoomDataMapper(DataMapper):
    db_model = RoomModel
    schema = RoomSchema


class RoomWithRelsDataMapper(DataMapper):
    db_model = RoomModel
    schema = RoomWithRels