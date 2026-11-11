from sqlalchemy import insert, select, update, delete
from pydantic import BaseModel

from src.repos.mappers.base import DataMapper



class BaseRepository():
    model = None
    mapper: DataMapper = None


    def __init__(self, session):
        self.session = session


    async def get_filtered(self, *filter, **filter_by) -> list[BaseModel]:
        query = (select(self.model)
            .filter(*filter)
            .filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        return [self.mapper.map_to_domain_entity(model) for model in result.scalars().all()]

    
    async def get_all(self, *args, **kwargs) -> list[BaseModel]:
        return await self.get_filtered()
    

    async def get_one_or_none(self, **filter_by) -> BaseModel | None:
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        return self.mapper.map_to_domain_entity(model) if model else None


    async def add(self, data: BaseModel) -> BaseModel:
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.mapper.map_to_domain_entity(model)


    async def add_bulk(self, data: list[BaseModel]):
        query = insert(self.model).values([item.model_dump() for item in data])
        await self.session.execute(query)


    async def edit(self, data: BaseModel, exclude_unset: bool = True, **filter_by) -> None:
        query = update(self.model).filter_by(**filter_by).values(**data.model_dump(exclude_unset=exclude_unset))
        await self.session.execute(query)


    async def delete(self, **filter_by) -> None:
        query = delete(self.model).filter_by(**filter_by)
        await self.session.execute(query)