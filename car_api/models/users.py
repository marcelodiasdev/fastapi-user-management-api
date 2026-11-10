from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func

from car_api.models.base import Base

if TYPE_CHECKING:
    from car_api.models import Car


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    cars: Mapped[List['Car']] = relationship(back_populates='owner')
