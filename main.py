import logging
import asyncio
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import config
from random_fox import fox
from random import randint
from keyboards import kb1, kb2

API_TOKEN = config.token
WEATHER_API_KEY = config.weather_api_key  # Добавьте ключ API OpenWeatherMap в файл config.py

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его. Либо используй кнопки", reply_markup=kb1)

@dp.message(F.text.lower() == '/num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")
@dp.message(Command("fox"))
@dp.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    # await message.answer_photo(image_fox)
    await bot.send_photo(message.chat.id, image_fox)
    # await message.answer(f"{image_fox}")

@dp.message(Command("weather"))
async def get_weather(message: types.Message):
    await message.answer("Пожалуйста, отправьте свою геопозицию для получения данных о погоде.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [types.KeyboardButton(text="Отправить геопозицию", request_location=True)]
                             ],
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@dp.message(lambda message: message.location is not None)
async def handle_location(message: types.Message):
    location = message.location
    lat = location.latitude
    lon = location.longitude

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(weather_url)
    if response.status_code != 200:
        await message.answer("Не удалось получить данные о погоде.")
        return

    weather_data = response.json()
    city = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    weather_message = f"Погода в {city}: {weather_description}, температура {temperature}°C"
    await message.answer(weather_message, reply_markup=types.ReplyKeyboardRemove())


@dp.message(Command("anecdote"))
async def get_anecdote(message: types.Message):
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"
    response = requests.get(url)
    if response.status_code != 200:
        await message.answer("Не удалось получить анекдот.")
        return

    # Ответ приходит в неправильном формате JSON, поэтому необходимо его обработать
    response_text = response.text
    # Удаляем лишние символы для преобразования в корректный JSON
    response_text = response_text.strip().lstrip('[').rstrip(']').replace('\r', '').replace('\n', '')

    try:
        joke_data = eval(response_text)  # Используем eval для преобразования строки в словарь
        anecdote = joke_data['content']
    except Exception as e:
        await message.answer("Произошла ошибка при обработке анекдота.")
        logging.error(f"Error parsing joke data: {e}")
        return

    await message.answer(anecdote)

@dp.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer("УРАААА!")
    elif message.text == "инфо":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)




@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
