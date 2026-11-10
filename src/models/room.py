from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from src.db import Base



class RoomModel(Base):
    __tablename__ = "rooms"

    room_id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.hotel_id"))
    title: Mapped[str]
    description: Mapped[str | None] = mapped_column(String(500))
    price: Mapped[int]
    quantity: Mapped[int]

    facilities: Mapped[list["FacilityModel"]] = relationship(
    back_populates="rooms",
    secondary="room_facilities"
)