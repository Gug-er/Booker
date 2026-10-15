from fastapi import APIRouter, Body, Response, Request

from src.schemas.user import UserSchema, UserAdd, UserRequestAdd, UserLogin
from src.services.auth import AuthService
from src.api.deps.auth import UserDep
from src.api.deps.database import DBDep



router = APIRouter(prefix='/auth', tags=["Authorization, authentication"])


@router.post("/register")
async def register_user(
    db: DBDep,
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
    user = await db.user.add(_data)
    await db.commit()

    return {"status": "OK", "data": user}


@router.post("/login")
async def login_user(
    db: DBDep,
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
    user = await db.user.get_user_by_email(data.email)

    if not user:
        return {"status": "ERROR", "detail": "Invalid email or password"}
    else:
        if AuthService().verify_password(data.password, user.hashed_password):
            jwt_access_token = AuthService().create_access_token({"user_id": user.user_id,})
            response.set_cookie(key="jwt_access_token", value=jwt_access_token)
            return {"jwt_access_token": jwt_access_token}
        else:
            return {"status": "ERROR", "detail": "Invalid email or password"}


@router.get("/me")
async def get_me(
    user_id: UserDep,
    db: DBDep
):
    user = await db.user.get_one_or_none(user_id=user_id)
    return user


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("jwt_access_token")
    return {"status": "OK"}