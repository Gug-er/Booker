from fastapi import Depends
from typing import Annotated

from src.db import async_session_maker
from src.utils.db_manager import DBManager



async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]