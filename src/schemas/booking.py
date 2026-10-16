from datetime import date
from pydantic import BaseModel, ConfigDict



class BookingSchema(BaseModel):
    booking_id: int
    user_id: int
    room_id : int
    date_from: date
    date_to: date
    price: int

    model_config = ConfigDict(from_attributes=True)


class BookingAdd(BaseModel):
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    price: int


class BookingRequestAdd(BaseModel):
    room_id : int
    date_from: date
    date_to: date