import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8646044834:AAHVp-Xe8jBuwkZBQR42E2xl7gRRR25-Su0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки (4 штуки)
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас"), KeyboardButton(text="Услуги")],
        [KeyboardButton(text="Кейсы"), KeyboardButton(text="Связаться с нами")]
    ],
    resize_keyboard=True
)

@dp.message()
async def handler(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "Привет!👋 Добро пожаловать в мир Telegram-ботов. Я создаю ботов для Бизнеса, Магазина, Автосервисов, заявок и заказов, Ai и нейросетей! Хочешь собственного бота под свои задачи? Используй кнопки ниже)",
            reply_markup=keyboard
        )
    else:
        await message.answer("Кнопка не делает 😄")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
