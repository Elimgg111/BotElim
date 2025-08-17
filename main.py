from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

# Токен можно хранить в переменной окружения
TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN_HERE")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я простой бот на aiogram 🤖")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Ты написал: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)