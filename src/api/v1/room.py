from fastapi import APIRouter, Body, Query

from src.db import async_session_maker
from src.repos.room import RoomRepository
from src.schemas.room import RoomSchema, RoomAdd, RoomRequestAdd, RoomRequestPatch, RoomPatch


router = APIRouter(prefix="/hotels", tags=["rooms"])



@router.post("/{hotel_id}/rooms")
async def add_room(
    hotel_id: int,
    room_data: RoomRequestAdd = Body(
        openapi_examples={
            "1": {"summary": "Example room",
                  "value":{
                      "title": "2 person 1 bed",
                      "description": "Big room for two persons with one bed",
                      "price": "100",
                      "quantity": "4"
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
async def get_rooms(hotel_id: int) -> list[RoomSchema]:
    async with async_session_maker() as session:
        return await RoomRepository(session).get_filtered(
            hotel_id=hotel_id
        )


@router.get("/{hotel_id}/rooms/{room_id}")
async def get_room_by_id(hotel_id: int, room_id: int):
    async with async_session_maker() as session:
        return await RoomRepository(session).get_one_or_none(room_id=room_id, hotel_id=hotel_id)


@router.put("/{hotel_id}/rooms/{room_id}")
async def edit_room(hotel_id: int, room_id: int, room_data: RoomRequestPatch):
    _room_data = RoomPatch(room_id=room_id, hotel_id=hotel_id, **room_data.model_dump())
    async with async_session_maker() as session:
        await RoomRepository(session).edit(_room_data, room_id=room_id, hotel_id=hotel_id)
        await session.commit()

    return {"status": "OK"}


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room(hotel_id: int, room_id: int):
    async with async_session_maker() as session:
        await RoomRepository(session).delete(room_id=room_id, hotel_id=hotel_id)
        await session.commit()

    return {"status": "OK"}