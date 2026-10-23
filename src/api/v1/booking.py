from fastapi import APIRouter

from src.schemas.booking import BookingSchema, BookingAdd, BookingRequestAdd
from src.api.deps.database import DBDep
from src.api.deps.auth import UserDep



router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("")
async def get_bookings(
    db: DBDep,
):
    bookings = await db.booking.get_all()
    return {"status": "OK", "data": bookings}


@router.get("/me")
async def get_my_bookings(
    db: DBDep,
    user_id: UserDep,
):
    bookings = await db.booking.get_filtered(user_id=user_id)
    return {"status": "OK", "data": bookings}


@router.post("")
async def add_booking(
    db: DBDep,
    user_id: UserDep,
    booking_data: BookingRequestAdd
):
    room = await db.room.get_one_or_none(room_id=booking_data.room_id)
    room_price: int = room.price
    _booking_data = BookingAdd(
        user_id=user_id,
        price=room_price,
        **booking_data.model_dump()
    )
    booking = await db.booking.add(_booking_data)
    await db.commit()

    return {"status": "OK", "data": booking}