from pydantic import BaseModel, ConfigDict



class RoomSchema(BaseModel):
    room_id: int
    hotel_id: int
    title: str
    description: str | None = None
    price: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class RoomPatch(BaseModel):
    room_id: int
    hotel_id: int
    title: str
    description: str | None = None
    price: int
    quantity: int


class RoomRequestPatch(BaseModel):
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