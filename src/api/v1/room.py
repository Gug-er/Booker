from fastapi import APIRouter, Body, Query

from src.schemas.room import RoomSchema, RoomAdd, RoomRequestAdd, RoomRequestPatch, RoomPatch
from src.api.deps.database import DBDep



router = APIRouter(prefix="/hotels", tags=["rooms"])


@router.post("/{hotel_id}/rooms")
async def add_room(
    db: DBDep,
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
    room = await db.room.add(room_data)
    await db.commit()
    return {"status": "OK", "data": room}


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    db: DBDep,
    hotel_id: int
) -> list[RoomSchema]:
    return await db.room.get_filtered(
        hotel_id=hotel_id
    )


@router.get("/{hotel_id}/rooms/{room_id}")
async def get_room_by_id(
    db: DBDep,
    hotel_id: int, 
    room_id: int
):
    return await db.room.get_one_or_none(room_id=room_id, hotel_id=hotel_id)


@router.put("/{hotel_id}/rooms/{room_id}")
async def edit_room(
    db: DBDep,
    hotel_id: int, 
    room_id: int, 
    room_data: RoomRequestPatch
):
    _room_data = RoomPatch(room_id=room_id, hotel_id=hotel_id, **room_data.model_dump(exclude_unset=True))
    await db.room.edit(_room_data, room_id=room_id, hotel_id=hotel_id)
    await db.commit()

    return {"status": "OK"}


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room(
    db: DBDep,
    hotel_id: int, 
    room_id: int
):
    await db.room.delete(room_id=room_id, hotel_id=hotel_id)
    await db.commit()

    return {"status": "OK"}