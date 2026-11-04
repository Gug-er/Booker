from pydantic import BaseModel, ConfigDict



class FacilitySchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class FacilityAdd(BaseModel):
    name: str