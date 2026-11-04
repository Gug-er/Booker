from datetime import date

from src.repos.base import BaseRepository
from src.repos.utils import room_ids_for_booking
from src.models.room import RoomModel
from src.schemas.room import RoomSchema



class RoomRepository(BaseRepository):
    model = RoomModel
    schema = RoomSchema


    async def get_filtered_by_time(
        self, 
        date_from: date, 
        date_to: date,
        hotel_id: int | None = None
    ):
        available_room_ids = room_ids_for_booking(
            date_from=date_from, 
            date_to=date_to,
            hotel_id=hotel_id
            )
        
        return await self.get_filtered(RoomModel.room_id.in_(available_room_ids))