from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseModel



class UserModel(BaseModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]