from fastapi import APIRouter, Body

from src.schemas.hotel import HotelSchema, HotelAdd, HotelPatch

router = APIRouter(prefix="/hotel", tags=["hotel"])

@router.post("")
async def add_hotel(
    hotel_data: HotelAdd = Body(
        openapi_examples={
            "1": {"summary": "Some hotel in some city",
                  "value":{
                      "name": "Actual name of the hotel",
                      "title": "Unique name of the hotel",
                      "description": "It`s description"
                    }
                  }
        }
    )
) -> None:
    ...#db.hotel.add(hotel_data)


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
                    "title": "sas-sinai-continental-fivestar",
                    "description": "Beautiful hotel near the red sea"
                },
                {
                    "name": "Redison blue resort",
                    "title": "sas-sinai-redison-fivestar",
                    "description": "Beautiful hotel on the shores of red sea"
                }]
            }
})
) -> None:
    ...#db.hotel.add_bulk(hotel_data)


@router.get("")
async def get_list_of_hotels(page: int, per_page: int) -> list[HotelSchema]:
    ... 