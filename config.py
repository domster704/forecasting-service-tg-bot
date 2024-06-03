import json

from telebot import TeleBot

env: dict = json.load(open("env.json"))

bot = TeleBot(env["apiTG"])
