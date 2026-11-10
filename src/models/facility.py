from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from src.db import Base



class FacilityModel(Base):
    __tablename__ = "facilities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    rooms: Mapped[list["RoomModel"]] = relationship(
        back_populates="facilities",
        secondary="room_facilities"
    )


class RoomFacilityModel(Base):
    __tablename__ = "room_facilities"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"))
    facility_id: Mapped[int] = mapped_column(ForeignKey("facilities.id"))