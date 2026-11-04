from fastapi import APIRouter

from src.schemas.facility import FacilitySchema, FacilityAdd
from src.api.deps.database import DBDep



router = APIRouter(prefix="/facilities", tags=["facilities"])


@router.get("")
async def get_facilities(
        db: DBDep,
):
    return await db.facility.get_all()


@router.post("")
async def add_facility(
    db: DBDep,
    data: FacilityAdd
):
    facility = await db.facility.add(data)
    await db.commit()
    return {"status": "OK", "data": facility}