from pydantic import BaseModel, ConfigDict, EmailStr



class UserSchema(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class UserHashedPassword(UserSchema):
    hashed_password: str


class UserAdd(BaseModel):
    email: EmailStr
    hashed_password: str
    first_name: str
    last_name: str


class UserRequestAdd(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str