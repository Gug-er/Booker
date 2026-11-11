from datetime import date

from sqlalchemy import select, func

from src.repos.base import BaseRepository
from src.models.room import RoomModel
from src.models.hotel import HotelModel
from src.repos.mappers.hotel import HotelDataMapper
from src.repos.utils import room_ids_for_booking



class HotelRepository(BaseRepository):
    model = HotelModel
    mapper = HotelDataMapper


    async def get_filtered_by_time(
            self, 
            date_from: date, 
            date_to: date,
            location: str | None,
            name: str | None,
            limit: int, 
            offset: int
        ):
            room_ids_to_get = room_ids_for_booking(
                date_from=date_from, 
                date_to=date_to
                )

            hotel_ids_to_get = (
                 select(RoomModel.hotel_id)
                 .select_from(RoomModel)
                 .filter(RoomModel.room_id.in_(room_ids_to_get))
            )

            query = select(HotelModel).filter(HotelModel.hotel_id.in_(hotel_ids_to_get))
            if location:
                 query = query.filter(func.lower(HotelModel.location).contains(location.strip().lower()))
            if name:
                 query = query.filter(func.lower(HotelModel.name).contains(name.strip().lower()))
            query = (
                 query
                 .limit(limit)
                 .offset(offset) 
            )
            
            result = await self.session.execute(query)

            return [self.mapper.map_to_domain_entity(hotel) for hotel in result.scalars().all()]