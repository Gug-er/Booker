from pydantic import BaseModel, ConfigDict, Optional



class RoomSchema(BaseModel):
    room_id: int
    hotel_id: int
    title: str
    description: Optional[str] = None
    price: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class RoomPatch(BaseModel):
    room_id: int
    hotel_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None


class RoomRequestPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None


class RoomAdd(BaseModel):
    hotel_id: int
    title: str
    description: Optional[str] = None
    price: int
    quantity: int


class RoomRequestAdd(BaseModel):
    title: str
    description: Optional[str] = None
    price: int
    quantity: int