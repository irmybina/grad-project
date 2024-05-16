from aiogram import Bot, Dispatcher
import asyncio
from bot.handlers import router

async def main():
    bot = Bot(token='6761695320:AAEsLt-bdh7aX_YAZbktRlp-cX1bS7mTAd8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down")



