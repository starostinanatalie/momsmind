import time
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types, filters
from config_reader import config
from aiogram.utils.exceptions import BotBlocked
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Text

import os
import psycopg2

logging.basicConfig(level=logging.INFO)

# with open('credentials.txt', 'r', encoding='cp1252') as credentials:
#     for line in credentials:
#         TOKEN = line

MSG = "What we have for dinner today?"

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot=bot)

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id}{user_full_name}{time.asctime()}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Soup", "Main dish"]
    keyboard.add(*buttons)
    await message.reply(f'Hello, {user_name}, {MSG}', reply_markup=keyboard)

@dp.message_handler(Text(equals="Soup"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals="Main dish"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



