from pydantic import BaseModel, Field

class HotelSchema(BaseModel):
    hotel_id: int
    name: str
    location: str
    description: str | None = Field(None)


class HotelPatch(BaseModel):
    name: str | None = Field(None)
    location: str | None = Field(None)
    description: str | None = Field(None)


class HotelAdd(BaseModel):
    name: str
    location: str
    description: str | None = Field(None)