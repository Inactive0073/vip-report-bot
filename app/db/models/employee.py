from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseIDModel
from .mixins import TimestampMixin, TelegramProfileMixin

if TYPE_CHECKING:
    from .visit import Visit
    from .user import User

class Employee(TimestampMixin, TelegramProfileMixin, BaseIDModel):
    __tablename__ = "employees"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    visits: Mapped[list["Visit"]] = relationship(back_populates="employee")
    user: Mapped["User"] = relationship()
