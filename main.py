from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7828928358:AAEl0_jrNjaJPlPiAmha4RIJAXaE0i3N4EY')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Привет")

executor.start_polling(dp)