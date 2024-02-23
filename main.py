import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import load_dotenv
load_dotenv()

from components.connect_db import openServer
from handlers.users_menu import user_menu_router
# from handlers.admins_menu import admin_menu_router

bot = Bot(os.getenv("token"))
dp = Dispatcher(bot=bot)

dp.include_router(user_menu_router)

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("привет")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    openServer(host=os.getenv("host"), 
               user=os.getenv("user"), 
               password=os.getenv("password"), 
               database=os.getenv("db_name")
               )
    
    asyncio.run(main())