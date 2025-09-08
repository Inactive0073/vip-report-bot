from app.db.models.base_model import BaseIDModel
from .mixins import TimestampMixin, TelegramProfileMixin


class Admin(TimestampMixin, TelegramProfileMixin, BaseIDModel):
    __tablename__ = "admins"

    # created_at добавляется из миксина

    def __repr__(self) -> str:
        if self.last_name is None:
            name = self.first_name
        else:
            name = f"{self.first_name} {self.last_name}"
        return (
            f"[{self.telegram_id} | {self.username}] {name}"
        )
