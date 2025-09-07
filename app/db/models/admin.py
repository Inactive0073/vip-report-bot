from sqlalchemy import String, SmallInteger, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from .mixins import TimestampMixin, TelegramProfileMixin


class Admin(TimestampMixin, TelegramProfileMixin, Base):
    __tablename__ = "users"

    # created_at добавляется из миксина

    def __repr__(self) -> str:
        if self.last_name is None:
            name = self.first_name
        else:
            name = f"{self.first_name} {self.last_name}"
        return (
            f"[{self.telegram_id} | {self.username}] {name}"
        )
