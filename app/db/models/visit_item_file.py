from typing import TYPE_CHECKING
from sqlalchemy import (
    String,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from .base_model import BaseIDModel

if TYPE_CHECKING:
    from .visit_item import VisitItem


class VisitItemFile(TimestampMixin, BaseIDModel):
    __tablename__ = "visit_item_files"
    __table_args__ = (
        Index("idx_visit_item_file_visit_item", "visit_item_id"),
        Index("idx_visit_item_file_created_at", "created_at"),
    )

    visit_item_id: Mapped[int] = mapped_column(ForeignKey("visit_items.id"))
    file_id: Mapped[str] = mapped_column(String(100))
    file_type: Mapped[str] = mapped_column(String(50))

    visit_item: Mapped["VisitItem"] = relationship(back_populates="visit_item_file")