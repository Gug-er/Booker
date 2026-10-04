from pydantic import BaseModel, Field

class HotelSchema(BaseModel):
    hotel_id: int
    name: str
    title: str
    description: str | None = Field(None)


class HotelPatch(BaseModel):
    name: str | None = Field(None)
    title: str | None = Field(None)
    description: str | None = Field(None)


class HotelAdd(BaseModel):
    name: str
    title: str
    description: str | None = Field(None)