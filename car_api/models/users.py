from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from car_api.models.base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    update_at: Mapped[str] = mapped_column(
        onupdate=func.now(),server_default=func.now(),
    )   
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )