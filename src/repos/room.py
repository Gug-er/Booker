from datetime import date
from sqlalchemy import select, func

from src.repos.base import BaseRepository
from src.repos.utils import room_ids_for_booking
from src.models.room import RoomModel
from src.schemas.room import RoomSchema



class RoomRepository(BaseRepository):
    model = RoomModel
    schema = RoomSchema


    async def get_filtered_by_time(
        self, 
        hotel_id: int, 
        date_from: date, 
        date_to: date
    ):
        available_room_ids = room_ids_for_booking(hotel_id, date_from, date_to)
        
        return await self.get_filtered(RoomModel.room_id.in_(available_room_ids))