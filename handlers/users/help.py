from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp

@dp.message_handler(CommandHelp())
async def hello(message: types.Message):
    await message.answer('Список доступных команд:'
                         '\n/help - как сделать домашку по матеше'
                         '\n/activity - замес')
