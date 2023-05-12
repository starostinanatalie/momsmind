import time
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types, filters
from config_reader import config

import os
import psycopg2

logging.basicConfig(level=logging.INFO)

with open('credentials.txt', 'r', encoding='cp1252') as credentials:
    for line in credentials:
        TOKEN = line

MSG = "What we have for dinner today?"

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id}{user_full_name}{time.asctime()}')
    await message.reply(f'Hello, {user_name}, {MSG}')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



