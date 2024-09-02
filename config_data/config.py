from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту

@dataclass
class Config:
    tg_bot: TgBot

@dataclass
class Payments:
    payments_token: str   # Токен для платежей

def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )
def load_payments(path: str | None = None) -> Payments:
    env: Env = Env()
    env.read_env(path)

    return Payments(
        payments_token= env('PAYMENTS_TOKEN')
    )