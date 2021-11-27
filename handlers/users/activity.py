from aiogram import types
from aiogram.dispatcher import FSMContext
from states import LoginState
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

@dp.message_handler(state=LoginState.on_user_menu)
async def activity_keyboard(message: types.Message):
    add_activ = KeyboardButton("Создать мероприятие")
    search_activ = KeyboardButton("Посмотреть мероприятия")
    playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        add_activ).add(search_activ)
    await message.answer(text="Решай, педик",
                         reply_markup=playlists_markup, )