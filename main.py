# Default modules - Модули по умолчанию
import json
import random
from os import system
from time import sleep
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
import requests
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Created module - Созданный модуль
from core.config import TOKEN, ADMIN_ALIBEK, ADMIN_ALIBEK_INT
from core.static.stikers import S001, S002

system("clear")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["alibek"])
async def alibek(message: types.Message):
    markup_alibek =InlineKeyboardMarkup().add(
        InlineKeyboardButton("Python", url="https://www.python.org/"),
        InlineKeyboardButton("ITC", url="https://www.itcbootcamp.com/#/"),
        InlineKeyboardButton("History", url="https://ru.hexlet.io/courses/python-basics/lessons/history/theory_unit")
    )
    await message.answer("Enjoy", reply_markup=markup_alibek)
    markup_alibek1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Хорошего дня"), KeyboardButton("Секрет")
    )
    await message.reply_sticker(random.choice(S001), reply_markup=markup_alibek1)

@dp.message_handler(content_types=["text"])
async def day(message: types.Message):
    if message.text.lower() == "хорошего дня":
        await message.answer("И тебе того же!")
        await message.reply_sticker(random.choice(S002))

    if message.text.lower() == "секрет":
        photo_s = open("core/static/image/image123.jpeg", "rb")
        await message.answer_photo(photo=photo_s, caption="Вселенского секрета нет, ты чудо😇!")
        await message.reply_sticker(random.choice(S002))

if __name__ == "__main__":  
    executor.start_polling(dp)
