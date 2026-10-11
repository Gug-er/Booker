from typing import Annotated
from fastapi import Depends, Request, HTTPException

from src.services.auth import AuthService



def get_token(request: Request) -> str:
    token = request.cookies.get("jwt_access_token", None)
    if not token:
        raise HTTPException(status_code=401, detail="User is not authenticated")
    else:
        return token


def get_user_id_from_token(token: str = Depends(get_token)) -> int:
    data = AuthService().decode_access_token(token)
    user_id = data["user_id"]
    return user_id

UserDep = Annotated[int, Depends(get_user_id_from_token)]