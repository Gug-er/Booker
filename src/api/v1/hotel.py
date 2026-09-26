from fastapi import APIRouter

router = APIRouter(prefix="/hotel", tags=["hotel"])

@router.post("/")
async def hello_world():
    return("Hello world")