from sqlalchemy import select, func

from src.repos.base import BaseRepository
from src.models.hotel import HotelModel
from src.schemas.hotel import HotelSchema

class HotelRepository(BaseRepository):
    model = HotelModel
    schema = HotelSchema


    async def get_all(
            self, 
            location, 
            name, 
            limit, 
            offset
    ) -> list[HotelSchema]:
        query = select(HotelModel)
        if location:
            query = query.filter(func.lower(HotelModel.location).contains(location.strip().lower()))
        if name:
            query = query.filter(func.lower(HotelModel.name).contains(name).contains(name.strip().lower()))
        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return [self.schema.model_validate(object, from_attributes=True) for object in result.scalars().all()]