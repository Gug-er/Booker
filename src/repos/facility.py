from sqlalchemy import insert, select, delete

from src.repos.base import BaseRepository
from src.models.facility import FacilityModel, RoomFacilityModel
from src.schemas.facility import FacilitySchema, RoomFacilitySchema



class FacilityRepository(BaseRepository):
    model = FacilityModel
    schema = FacilitySchema


class RoomFacilityRepository(BaseRepository):
    model = RoomFacilityModel
    schema = RoomFacilitySchema


    async def set_room_facilities(self, room_id: int, facility_ids: list[int]):
        get_current_facility_ids = (
            select(self.model.facility_id)
            .filter_by(room_id=room_id)
        )
        result = await self.session.execute(get_current_facility_ids)
        current_facility_ids: list[int] = result.scalars().all()
        ids_to_remove = list[int](set(current_facility_ids) - set(facility_ids))
        ids_to_add = list[int](set(facility_ids) - set(current_facility_ids))

        if ids_to_remove:
            delete_room_facilities = (
                delete(self.model)
                .filter(
                    self.model.room_id == room_id,
                    self.model.facility_id.in_(ids_to_remove)
                )
            )
            await self.session.execute(delete_room_facilities)
            
        if ids_to_add:
            add_room_facilities = (
                insert(self.model)
                .values([{"room_id": room_id, "facility_id": facility_id} for facility_id in ids_to_add])
            )
            await self.session.execute(add_room_facilities)
        