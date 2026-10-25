from sqlalchemy import insert, select, update, delete
from pydantic import BaseModel



class BaseRepository():
    model = None
    schema: BaseModel = None


    def __init__(self, session):
        self.session = session


    async def get_filtered(self, *filter, **filter_by) -> list[BaseModel]:
        query = (select(self.model)
            .filter(*filter)
            .filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        return [self.schema.model_validate(model) for model in result.scalars().all()]

    
    async def get_all(self, *args, **kwargs) -> list[BaseModel]:
        return await self.get_filtered()
    

    async def get_one_or_none(self, **filter_by) -> BaseModel | None:
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model =  result.scalars().one_or_none()
        return self.schema.model_validate(model)


    async def add(self, data: BaseModel) -> BaseModel:
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.schema.model_validate(model)


    async def edit(self, data: BaseModel, exclude_unset: bool = True, **filter_by) -> None:
        query = update(self.model).filter_by(**filter_by).values(**data.model_dump(exclude_unset=exclude_unset))
        await self.session.execute(query)


    async def delete(self, **filter_by) -> None:
        query = delete(self.model).filter_by(**filter_by)
        await self.session.execute(query)