from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states import LoginState, CreateActivityStates
import config.keyboards as keyboards
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(f'Привет, я бот Эковектора!'
                         f'\nЧем могу помочь?', reply_markup=keyboards.initialization(message))


@dp.callback_query_handler(text_contains='menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.answer('Список доступных команд:'
                                      '\n/help - список доступных команд'
                                      '\n/activity - недоступно')
        if code == 2:
            await call.message.answer('Отлично, перейдем к регистрации, напиши свой почтовый ящик')

        if code == 3:
            await call.message.answer(text="Что ты хочешь сделать?",
                                      reply_markup=keyboards.menu(), )


@dp.message_handler(text='Создать мероприятие', state='*')
async def add_activity(message: types.Message):
    await CreateActivityStates.on_start_creating.set()
    await message.answer('Отлично! Заполни небольшую анкету в формате:'
                         '\n1.Название мероприятия: Название'
                         '\n2.Дата провередения: дд.мм.гггг'
                         '\n3.Время проведения: чч:мм'
                         '\n4.Место проведения: Номер кабинета или локации'
                         '\n5.Краткое описание: ')


@dp.message_handler(state=CreateActivityStates.on_start_creating)
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        print(message.text)
    await state.finish()

@dp.message_handler(text='Посмотреть мероприятия', state='*')
async def add_activity(message: types.Message):
    await message.answer('Вот мероприятия, которые могут тебя заинтересовать:)')
