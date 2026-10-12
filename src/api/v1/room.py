from fastapi import APIRouter, Body, Query

from src.db import async_session_maker
from src.repos.room import RoomRepository
from src.schemas.room import RoomSchema, RoomAdd, RoomRequestAdd, RoomPatch


router = APIRouter(prefix="/hotels", tags=["rooms"])



@router.post("/{hotel_id}/rooms")
async def add_room(
    hotel_id: int,
    room_data: RoomRequestAdd = Body(
        openapi_examples={
            "1": {"summary": "Add room to the database",
                  "value":{
                      "title": "2 person"
                    }
                  }
        }
    )
) -> None:
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    async with async_session_maker() as session:
        room = await RoomRepository(session).add(room_data)
        await session.commit()
    return {"status": "OK", "data": room}


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    name: str | None = Query(None, description="Hotel name"),
    location: str | None = Query(None, description="Hotel location"),
) -> list[RoomSchema]:
    async with async_session_maker() as session:
        return await RoomRepository(session).get_all(
            location=location, 
            name=name, 
        )


@router.get("/{hotel_id}/rooms/{room_id}")
async def get_room_by_id(hotel_id: int, room_id: int):
    async with async_session_maker() as session:
        return await RoomRepository(session).get_one_or_none(room_id=room_id)


@router.put("/{hotel_id}/rooms/{room_id}")
async def edit_room(room_id: int, room_data: RoomPatch):
    async with async_session_maker() as session:
        await RoomRepository(session).edit(room_data, room_id=room_id)
        await session.commit()

    return {"status": "OK"}


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room(room_id: int):
    async with async_session_maker() as session:
        await RoomRepository(session).delete(room_id=room_id)
        await session.commit()

    return {"status": "OK"}