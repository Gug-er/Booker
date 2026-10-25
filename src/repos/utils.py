from datetime import date

from sqlalchemy import select, func

from src.models.room import RoomModel
from src.models.booking import BookingModel



def room_ids_for_booking(
        hotel_id: int,
        date_from: date,
        date_to: date,
):
    rooms_count = (
                select(RoomModel.room_id, func.count("*").label("rooms_booked"))
                .select_from(RoomModel)
                .filter(
                    BookingModel.date_from <= date_to,
                    BookingModel.date_to >= date_from, 
                )
                .group_by(RoomModel.room_id)
                .cte("rooms_count")
            )
    
    rooms_available = (
        select(
            RoomModel.room_id,
            (RoomModel.quantity - func.coalesce(rooms_count.c.rooms_booked, 0)).label("rooms_left"),
            )
        .select_from(RoomModel)
        .outerjoin(rooms_count, RoomModel.room_id == rooms_count.c.room_id)
        .cte("rooms_available")
    )

    rooms_by_hotel_id = (
        select(RoomModel.room_id)
        .select_from(RoomModel)
        .filter_by(hotel_id=hotel_id)
        .subquery(name="rooms_by_hotel_id")
    ) 

    available_room_ids = (
        select(rooms_available.c.room_id)
        .select_from(rooms_available)
        .filter(
            rooms_available.c.rooms_left > 0,
            rooms_available.c.room_id.in_(rooms_by_hotel_id)
            )
    )

    return available_room_ids
