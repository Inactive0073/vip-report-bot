from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseIDModel
from .mixins import TimestampMixin, TelegramProfileMixin

class User(TimestampMixin, TelegramProfileMixin, BaseIDModel):
    __tablename__ = "users"

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_employee: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        name = f"{self.first_name} {self.last_name}" if self.last_name else self.first_name
        return f"User[{self.telegram_id} | {self.username}] {name}"