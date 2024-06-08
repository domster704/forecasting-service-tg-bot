from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import dp, setAppState
from res.info_text import *
from res.login_text import TRANSITION_BUTTON_TEXT
from state.general_state import AppState

infoRouter = Router()


# @infoRouter.message(F.text == USER_INFO_BUTTON_TEXT)
@infoRouter.message(AppState.info, F.text == TRANSITION_BUTTON_TEXT)
async def infoHandlerInit(message: Message, state: FSMContext):
    await setAppState(state, AppState.info)

    keyboard = ReplyKeyboardBuilder().add(
        KeyboardButton(text=CONTINUE_BUTTON_TEXT)
    ).row(
        KeyboardButton(text=USER_INFO_BUTTON_TEXT),
        KeyboardButton(text=HELP_BUTTON_TEXT)
    )

    await message.answer(text=INFO_TEXT, reply_markup=keyboard.as_markup(resize_keyboard=True))


@infoRouter.message(F.text == HELP_BUTTON_TEXT)
async def getHelp(message):
    print(1)
    await message.reply(text=HELP_TEXT)

# @infoRouter.message(F.text == BACK_BUTTON_TEXT)
# def get_help(message, error):
#     if type(error) is PermissionError:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         retry_button = types.KeyboardButton(text=TRY_AUTH_MESSAGE)
#         markup.add(retry_button)
#
#         bot.send_message(message.chat.id, PERMISSION_ERROR_TEXT, parse_mode='html', reply_markup=markup)
#         return
