from aiogram import types
import config.keyboards as keyboards
from aiogram.dispatcher import FSMContext
from states import CreateActivityStates
from .escape import escape_creation
import config.activity_dict as ad


async def new_create(next_question, new_state, message: types.Message, state: FSMContext):
    if message.text == 'Отменить создание':
        await escape_creation(message, state)
    else:
        await new_state
        await ad.mk_dict(message, state)
        await message.answer(next_question, reply_markup=keyboards.escape_button())

# 'Теперь напишите дату в формате(гггг-мм-дд чч:мм)' 'name'
