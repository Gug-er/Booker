import uvicorn
from fastapi import FastAPI

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.api.v1.hotel import router as hotel_router


app = FastAPI()

app.include_router(hotel_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)