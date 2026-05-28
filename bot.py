import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8646044834:AAHVp-Xe8jBuwkZBQR42E2xl7gRRR25-Su0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки (4 штуки)
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
        [KeyboardButton(text="Кнопка 3"), KeyboardButton(text="Кнопка 4")]
    ],
    resize_keyboard=True
)

@dp.message()
async def handler(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "Привет! Это тестовый бот 👋",
            reply_markup=keyboard
        )
    else:
        await message.answer("Кнопка нажата (но она ничего не делает 😄)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
