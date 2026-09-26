from pydantic import BaseModel, Field

class HotelSchema(BaseModel):
    hotel_id: int
    title: str
    description: str | None = Field(None)


class HotelPatch(BaseModel):
    title: str | None = Field(None)
    description: str | None = Field(None)