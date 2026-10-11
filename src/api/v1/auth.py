from fastapi import APIRouter, Body, Response

from src.schemas.user import UserSchema, UserAdd, UserRequestAdd, UserLogin
from src.repos.user import UserRepository
from src.db import async_session_maker
from src.services.auth import AuthService


router = APIRouter(prefix='/auth', tags=["Authorization, authentication"])



@router.post("/register")
async def register_user(
    data: UserRequestAdd = Body(
        openapi_examples={
            "1": {"summary": "Example",
                  "value":{
                      "email": "example@mail.com",
                      "password": "exampleuser!",
                      "first_name": "Example",
                      "last_name": "User"
                    }
                 }
        }
    )
):
    hashed_password = AuthService().hash_password(data.password)
    _data = UserAdd(
        email=data.email, 
        hashed_password=hashed_password, 
        first_name=data.first_name,
        last_name=data.last_name
        )
    async with async_session_maker() as session: 
        user = await UserRepository(session).add(_data)
        await session.commit()

    return {"status": "OK", "data": user}


@router.post("/login")
async def login_user(
    response: Response,
    data: UserLogin = Body(
        openapi_examples={
            "1": {"summary": "Example",
                  "value":{
                      "email": "example@mail.com",
                      "password": "exampleuser!",
                    }
                 }
        }
    )
):
    async with async_session_maker() as session:
        user = await UserRepository(session).get_user_by_email(data.email)

    if not user:
        return {"status": "ERROR", "detail": "Invalid email or password"}
    else:
        if AuthService().verify_password(data.password, user.hashed_password):
            jwt_access_token = AuthService().create_access_token({"user_id": user.user_id,})
            response.set_cookie(key="jwt_access_token", value=jwt_access_token)
            return {"jwt_access_token": jwt_access_token}
        else:
            return {"status": "ERROR", "detail": "Invalid email or password"}
