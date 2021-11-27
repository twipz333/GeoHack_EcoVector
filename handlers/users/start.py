from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import LoginState
from handlers.users.activity import activity_keyboard

from loader import dp

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    if message.chat.id != 443808849: # проверка регистрации
        menu_1 = InlineKeyboardButton(text='Помощь', callback_data="menu_1")
        menu_2 = InlineKeyboardButton(text='Регистрация', callback_data="menu_2")
        keyboard.add(menu_1, menu_2)
    else:
        menu_1 = InlineKeyboardButton(text='Помощь', callback_data="menu_1")
        menu_3 = InlineKeyboardButton(text='Главное меню', callback_data="menu_3")
        keyboard.add(menu_1, menu_3)
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
            await LoginState.on_registation_menu.set()
        if code == 3:
            await call.message.answer('Добро пожаловать',)
            await LoginState.on_user_menu.set()

