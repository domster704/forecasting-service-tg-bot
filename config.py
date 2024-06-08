import json

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import sessionmaker

from db.db import engine, User
from state.general_state import AppState

__env: dict = json.load(open("env.json"))

bot = Bot(token=__env["apiTG"],
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML
          ))
dp = Dispatcher()

__Session = async_sessionmaker(bind=engine)
session = __Session()


async def setAppState(state: FSMContext, state_value: State):
    await state.set_state(state_value)
    appState = await state.get_data()
    for key, value in appState.items():
        appState[key] = False

    appState[state_value.state.split(":")[-1].lower()] = True

    await state.set_data(appState)
    print(await state.get_data())
