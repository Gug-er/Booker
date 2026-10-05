from fastapi import APIRouter, Body, Query

from sqlalchemy import insert

from src.models.hotel import HotelModel

from src.api.deps.pagination import PaginationDep
from src.schemas.hotel import HotelSchema, HotelAdd, HotelPatch
from src.db import async_session_maker

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
        add_hotel_stmt = insert(HotelModel).values(**hotel_data.model_dump())
        await session.execute(add_hotel_stmt)
        await session.commit()
    #db.hotel.add(hotel_data)


@router.post("")
async def add_bulk_hotel(
    hotel_data: list[HotelAdd] = Body(
        openapi_examples={
        "1":
            {
                "summary": "List of hotels",
                "value":[
                {
                    "name": "Continental plaza beach resort",
                    "location": "Country, city",
                    "description": "Beautiful hotel near the red sea"
                },
                {
                    "name": "Redison blue resort",
                    "location": "Country, city",
                    "description": "Beautiful hotel on the shores of red sea"
                }]
            }
})
) -> None:
    ...#db.hotel.add_bulk(hotel_data)


@router.get("")
async def get_hotels(
    pagination: PaginationDep,
    id: int | None = Query(None, description="Hotel id"),
    name: str | None = Query(None, description="Hotel name"),
    lcoation: str | None = Query(None, description="Hotel location"),
) -> list[HotelSchema]:
    ...