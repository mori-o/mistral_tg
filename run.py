import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router


# Создаем асинхронную функцию
async def main():
    # Подгрузка переменных
    load_dotenv()

    # Инициализация объекта бот, передача токена
    bot = Bot(token=os.getenv('TG_TOKEN'))

    # Инициализация диспетчера
    dispatcher = Dispatcher()

    # Так как основные методы будут в handlers.py, работаем с router
    dispatcher.include_router(router)

    # Асинхронный запуск функции через диспетчер
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is off')
