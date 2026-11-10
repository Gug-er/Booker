from fastapi import APIRouter, Body, Query
from datetime import date

from src.schemas.room import RoomSchema, RoomAdd, RoomRequestAdd, RoomRequestPatch, RoomPatch
from src.schemas.facility import RoomFacilityAdd
from src.api.deps.database import DBDep



router = APIRouter(prefix="/hotel", tags=["rooms"])


@router.get("/rooms")
async def get_rooms(
    db: DBDep,
    date_from: date = Query(
        openapi_examples={"2026-11-20": {
            "summary": "Example date from", 
            "value": "2026-11-20"}}),
    date_to: date = Query(
        openapi_examples={"2026-11-30": {
            "summary": "Example date to", 
            "value": "2026-11-30"}}),
    hotel_id: int | None = None,
):
    return await db.room.get_filtered_by_time(
        hotel_id=hotel_id,
        date_from=date_from,
        date_to=date_to
    )


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
                      "quantity": "4",
                      "facility_ids": [1, 2, 3]
                    }
                  }
        }
    )
):
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    room = await db.room.add(_room_data)

    room_facilities_data = [RoomFacilityAdd(room_id=room.room_id, facility_id=facility_id) for facility_id in room_data.facility_ids or []]
    await db.room_facility.add_bulk(room_facilities_data)

    await db.commit()
    return {"status": "OK", "data": room}


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
    room_data: RoomRequestAdd
):
    _room_data = RoomPatch(room_id=room_id, hotel_id=hotel_id, **room_data.model_dump(exclude_unset=True))
    await db.room.edit(_room_data, room_id=room_id)
    await db.room_facility.set_room_facilities(room_id=room_id, facility_ids=room_data.facility_ids)
    await db.commit()

    return {"status": "OK"}


@router.patch("/{hotel_id}/rooms/{room_id}")
async def edit_room_partially(
    db: DBDep,
    hotel_id: int, 
    room_id: int, 
    room_data: RoomRequestPatch
):
    room_data_dict = room_data.model_dump(exclude_unset=True)
    _room_data = RoomPatch(room_id=room_id, hotel_id=hotel_id, **room_data_dict)
    await db.room.edit(_room_data, room_id=room_id, hotel_id=hotel_id)
    if "facility_ids" in room_data_dict:
        await db.room_facility.set_room_facilities(room_id=room_id, facility_ids=room_data_dict["facility_ids"])
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