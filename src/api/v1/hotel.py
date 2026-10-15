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
) -> None:
    hotel = await db.hotel.add(hotel_data)
    await db.commit.commit()
    return {"status": "OK", "data": hotel}


@router.get("/hotels")
async def get_hotels(
    db: DBDep,
    pagination: PaginationDep,
    name: str | None = Query(None, description="Hotel name"),
    location: str | None = Query(None, description="Hotel location"),
) -> list[HotelSchema]:
    per_page = pagination.per_page or 5
    page = pagination.page or 1
    return await db.hotel.get_all(
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
) -> None:
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