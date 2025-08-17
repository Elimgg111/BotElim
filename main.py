import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import os

TOKEN = os.getenv("BOT_TOKEN", "7828928358:AAEl0_jrNjaJPlPiAmha4RIJAXaE0i3N4EY")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот на aiogram 3 🤖")

@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__": 1
    asyncio.run(main())
