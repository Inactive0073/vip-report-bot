from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class RedisConfig:
    host: str
    port: int
    db: str
    password: str


@dataclass
class DataBase:
    dsn: str
    is_echo: bool


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase
    redis_config: RedisConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path, override=True)
    return Config(
        tg_bot=TgBot(token=env("BOT_TOKEN")),
        db=DataBase(dsn=env("DSN"), is_echo=env.bool(("IS_ECHO"))),
        redis_config=RedisConfig(
            host=env("REDIS_HOST"),
            port=env("REDIS_PORT"),
            db=env("REDIS_DB"),
            password=env("REDIS_PASSWORD")
            ),
    )
