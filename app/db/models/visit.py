from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base_model import BaseIDModel
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .employee import Employee
    from .point import Point
    from .visit_item import VisitItem

class Visit(TimestampMixin, BaseIDModel):
    __tablename__ = "visits"

    __table_args__ = (
        Index("idx_visit_created_at", "created_at"),
        Index("idx_visit_employee_point", "employee_id", "point_id"),
    )

    description: Mapped[str] = mapped_column(String(500))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    point_id: Mapped[int] = mapped_column(ForeignKey("points.id"))
    
    employee: Mapped["Employee"] = relationship(back_populates="visits")
    point: Mapped["Point"] = relationship(back_populates="visits")
    visit_items: Mapped[list["VisitItem"]] = relationship(back_populates="visit")

    def __repr__(self) -> str:
        return f"ID {self.id}\nОписание: {self.description}\nСотрудник: {self.employee_id}\nТочка: {self.point_id}"