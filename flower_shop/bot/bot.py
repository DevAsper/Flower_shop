from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

# Настройки бота
API_TOKEN = '7380778143:AAEWKhL7YRSE7mOkKo313-saUdOGPc1CvMk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Это бот цветочного магазина.")

# Функция для отправки уведомления о заказе
async def send_order_notification(chat_id, order_info):
    await bot.send_message(chat_id, f"Новый заказ:\n{order_info}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
