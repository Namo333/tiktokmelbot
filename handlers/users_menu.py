from aiogram import types, Router
from aiogram.filters import Command

user_menu_router=Router()

@user_menu_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Я меню")