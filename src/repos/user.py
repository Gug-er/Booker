from pydantic import EmailStr
from sqlalchemy import select

from src.repos.base import BaseRepository
from src.models.user import UserModel
from src.repos.mappers.user import UserDataMapper, UserHashedPasswordDataMapper



class UserRepository(BaseRepository):
    model = UserModel
    mapper = UserDataMapper


    async def get_user_by_email(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model:
            return UserHashedPasswordDataMapper.map_to_domain_entity(model)
        else:
            return None