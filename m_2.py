# import logging
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters.command import Command
# import config
# from random_fox import fox
# from keyboards import kb1, kb2
# from random import randint
#
#
# API_TOKEN = config.token
#
# # Включаем логирование, чтобы видеть сообщения в консоли
# logging.basicConfig(level=logging.INFO)
#
# # Инициализация бота и диспетчера
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def command_start(message: types.Message):
#     await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=kb1)
#
#
# @dp.message(Command("ура"))
# async def send_ura(message: types.Message):
#     await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=kb2)
#
#
# @dp.message(Command("fox"))
# @dp.message(Command("лиса"))
# async def send_fox(message: types.Message):
#     image_fox = fox()
#     # await message.answer_photo(image_fox)
#     await bot.send_photo(message.chat.id, image_fox)
#     # await message.answer(f"{image_fox}")
#
#
# @dp.message(F.text.lower() == 'num')
# async def send_random(message: types.Message):
#     number = randint(1, 10)
#     await message.answer(f"{number}")
#
#
# @dp.message(F.text)
# async def echo(message: types.Message):
#     if "ура" in message.text:
#         await message.answer("УРАААА!")
#     elif message.text == "инфо":
#
#         user_name = message.chat.id
#         print(user_name)
#         await message.answer(str(user_name))
#     else:
#         await message.answer(message.text)
#
#
#
#
#
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())