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

    visits: Mapped[list["Visit"]] = relationship(back_populates="employee", lazy="selectin")
