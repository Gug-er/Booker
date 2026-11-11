from src.repos.mappers.base import DataMapper
from src.models.user import UserModel
from src.schemas.user import UserSchema, UserHashedPassword



class UserDataMapper(DataMapper):
    db_model = UserModel
    schema = UserSchema


class UserHashedPasswordDataMapper(DataMapper):
    db_model = UserModel
    schema = UserHashedPassword