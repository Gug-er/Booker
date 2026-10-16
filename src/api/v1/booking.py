from fastapi import APIRouter

from src.schemas.booking import BookingAdd, BookingRequestAdd
from src.api.deps.database import DBDep
from src.api.deps.auth import UserDep



router = APIRouter(prefix="/bookings", tags=["bookings"])


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