from typing import TYPE_CHECKING
from sqlalchemy import (
    String,
    Integer,
    text,
    SmallInteger,
    BigInteger,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from .mixins import TimestampMixin
from .base_model import BaseIDModel

if TYPE_CHECKING:
    from .employee import Employee
    from .visit import Visit
    from .visit_item_file import VisitItemFile


class VisitItem(TimestampMixin, BaseIDModel):
    __tablename__ = "visit_items"
    __table_args__ = (
        Index("idx_visit_item_visit_id", "visit_id"),
        Index("idx_visit_item_created_at", "created_at"),
    )

    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int | None]
    quantity: Mapped[int | None]

    visit_item_file: Mapped[list["VisitItemFile"]] = relationship(
        back_populates="visit_item"
    )
    visit: Mapped["Visit"] = relationship(back_populates="visit_items")
