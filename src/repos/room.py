from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.repos.base import BaseRepository
from src.repos.utils import room_ids_for_booking
from src.models.room import RoomModel
from src.schemas.room import RoomSchema, RoomWithRels



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
        
        query = (
            select(self.model)
            .options(joinedload(self.model.facilities))
            .filter(RoomModel.room_id.in_(available_room_ids))
        )
        result = await self.session.execute(query)
        return [RoomWithRels.model_validate(model) for model in result.unique().scalars().all()]
    