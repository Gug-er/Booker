from pydantic import BaseModel, ConfigDict



class HotelSchema(BaseModel):
    hotel_id: int
    name: str
    location: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)


class HotelPatch(BaseModel):
    name: str | None = None
    location: str | None = None
    description: str | None = None


class HotelAdd(BaseModel):
    name: str
    location: str
    description: str | None = None