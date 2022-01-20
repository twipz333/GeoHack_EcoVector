from aiogram import types
import config.keyboards as keyboards
from aiogram.dispatcher import FSMContext


async def escape_creation(message: types.Message, state: FSMContext):
    await message.answer(f'Создание отменено'
                         f'\nЧем могу помочь?', reply_markup=keyboards.initialization(message))
    await state.finish()
