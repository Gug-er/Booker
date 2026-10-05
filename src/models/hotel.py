from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.db import BaseModel


class HotelModel(BaseModel):
    __tablename__ = "hotels"

    hotel_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
