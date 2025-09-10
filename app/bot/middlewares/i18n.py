from collections.abc import Awaitable, Callable
from typing import Any, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from fluent.runtime import FluentLocalization

from app.locales.i18n_format import I18N_FORMAT_KEY


class I18nMiddleware(BaseMiddleware):
    def __init__(
        self,
        l10ns: dict[str, FluentLocalization],
        default_lang: str,
    ):
        super().__init__()
        self.l10ns = l10ns
        self.default_lang = default_lang

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # some language/locale retrieving logic
        if not isinstance(event, (Message, CallbackQuery)):
            return await handler(event, data)
        if event.from_user:
            lang = event.from_user.language_code
        else:
            lang = self.default_lang
        if lang not in self.l10ns:
            lang = self.default_lang

        l10n = self.l10ns[lang]
        # we use fluent.runtime here, but you can create custom functions
        data[I18N_FORMAT_KEY] = l10n.format_value

        return await handler(event, data)
