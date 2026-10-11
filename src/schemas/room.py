from pydantic import BaseModel



class RoomSchema(BaseModel):
    room_id: int
    hotel_id: int
    title: str
    description: str | None = None
    price: int
    quantity: int


class RoomPatch(BaseModel):
    room_id: int
    hotel_id: int
    title: str
    description: str | None = None
    price: int
    quantity: int


class RoomAdd(BaseModel):
    hotel_id: int
    title: str
    description: str | None = None
    price: int
    quantity: int


class RoomRequestAdd(BaseModel):
    title: str
    description: str | None = None
    price: int
    quantity: int