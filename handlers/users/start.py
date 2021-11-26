from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp

keyboard = InlineKeyboardMarkup()
menu_1 = InlineKeyboardButton(text='Помощь', callback_data="menu_1")
menu_2 = InlineKeyboardButton(text='Я новенький', callback_data="menu_2")
menu_3 = InlineKeyboardButton(text='Я уже смешарик', callback_data="menu_3")
keyboard.add(menu_1, menu_2, menu_3)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, я хочу пива и чипсов'
                         f'\nА ты хочешь?', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer('Список доступных команд:'
                                      '\n/help - как сделать домашку по матеше'
                                      '\n/activity - замес')
        if code == 2:
            await call.message.answer('Отлично, перейдем к регистрации')
        if code == 3:
            await call.message.answer('Добро пожаловать')

