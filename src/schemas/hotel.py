from pydantic import BaseModel, ConfigDict, Optional



class HotelSchema(BaseModel):
    hotel_id: int
    name: str
    location: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class HotelPatch(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class HotelAdd(BaseModel):
    name: str
    location: str
    description: Optional[str] = None