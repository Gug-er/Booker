from pydantic import BaseModel, ConfigDict



class FacilitySchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class FacilityAdd(BaseModel):
    name: str


class RoomFacilitySchema(BaseModel):
    id: int
    room_id: int
    facility_id: int

    model_config = ConfigDict(from_attributes=True)


class RoomFacilityAdd(BaseModel):
    room_id: int
    facility_id: int