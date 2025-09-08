from typing import TYPE_CHECKING
from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base_model import BaseIDModel
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .visit import Visit


class Point(TimestampMixin, BaseIDModel):
    __tablename__ = "points"
    __table_args__ = (
        Index("idx_point_status", "status"),
    )

    name: Mapped[str]
    status: Mapped[str | None]
    address: Mapped[str]


    visits: Mapped[list["Visit"]] = relationship(back_populates="point")
    def __repr__(self) -> str:
        return f"Точка {self.name}\nАдрес: {self.address}\nСтатус: {self.status}"