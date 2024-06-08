import json

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import sessionmaker

from db.db import engine, User

__env: dict = json.load(open("env.json"))

bot = Bot(token=__env["apiTG"],
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML
          ))
dp = Dispatcher()

__Session = async_sessionmaker(bind=engine)
session = __Session()

