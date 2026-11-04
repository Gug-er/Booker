from datetime import date

from fastapi import APIRouter, Body, Query

from src.schemas.hotel import HotelSchema, HotelAdd, HotelPatch
from src.api.deps.pagination import PaginationDep
from src.api.deps.database import DBDep



router = APIRouter(prefix="/hotels", tags=["hotels"])


@router.post("")
async def add_hotel(
    db: DBDep,
    hotel_data: HotelAdd = Body(
        openapi_examples={
            "1": {"summary": "Add hotel to the database",
                  "value":{
                      "name": "Hotel",
                      "location": "Country, city",
                      "description": "Description"
                    }
                  }
        }
    )
):
    hotel = await db.hotel.add(hotel_data)
    await db.commit()
    return {"status": "OK", "data": hotel}


@router.get("")
async def get_hotels(
    db: DBDep,
    pagination: PaginationDep,
    name: str | None = Query(None, description="Hotel name"),
    location: str | None = Query(None, description="Hotel location"),
    date_from: date | None = Query(example="2026-11-20", description="Date from"),
    date_to: date | None = Query(example="2026-11-30", description="Date to"),
) -> list[HotelSchema]:
    per_page = pagination.per_page or 5
    page = pagination.page or 1
    return await db.hotel.get_filtered_by_time(
        date_from=date_from,
        date_to=date_to,
        location=location,
        name=name, 
        limit=per_page, 
        offset=per_page * (page - 1)
    )


@router.get("/{hotel_id}")
async def get_hotel_by_id(
    db: DBDep, 
    hotel_id: int
):
    return await db.hotel.get_one_or_none(hotel_id=hotel_id)



@router.put("/{hotel_id}")
async def edit_hotel(
    db: DBDep,
    hotel_id: int, 
    hotel_data: HotelPatch
):
    await db.hotel.edit(hotel_data, hotel_id=hotel_id)
    await db.commit()

    return {"status": "OK"}


@router.delete("/{hotel_id}")
async def delete_hotel(
    db: DBDep,
    hotel_id: int
):
    await db.hotel.delete(hotel_id=hotel_id)
    await db.commit()

    return {"status": "OK"}