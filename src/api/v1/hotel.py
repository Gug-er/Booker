from fastapi import APIRouter, Body, Query

from sqlalchemy import insert

from src.models.hotel import HotelModel

from src.api.deps.pagination import PaginationDep
from src.schemas.hotel import HotelSchema, HotelAdd, HotelPatch
from src.db import async_session_maker

from src.repos.hotel import HotelRepository

router = APIRouter(prefix="/hotel", tags=["hotel"])

@router.post("")
async def add_hotel(
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
    async with async_session_maker() as session:
        hotel = await HotelRepository(session).add(hotel_data)
        await session.commit()
    return {"status": "OK", "data": hotel}


@router.get("")
async def get_hotels(
    pagination: PaginationDep,
    id: int | None = Query(None, description="Hotel id"),
    name: str | None = Query(None, description="Hotel name"),
    lcoation: str | None = Query(None, description="Hotel location"),
) -> list[HotelSchema]:
    async with async_session_maker() as session:
        return await HotelRepository(session).get_all()


@router.get("/{hotel_id}")
async def get_hotel_by_id(hotel_id: int):
    async with async_session_maker() as session:
        return await HotelRepository(session).get_one_or_none(hotel_id=hotel_id)



@router.put("/{hotel_id}")
async def edit_hotel(hotel_id: int, hotel_data: HotelPatch):
    async with async_session_maker() as session:
        await HotelRepository(session).edit(hotel_data, hotel_id=hotel_id)
        await session.commit()

    return {"status": "OK"}


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: int):
    async with async_session_maker() as session:
        await HotelRepository(session).delete(hotel_id=hotel_id)
        await session.commit()

    return {"status": "OK"}