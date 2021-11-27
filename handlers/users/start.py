from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states import LoginState, CreateActivityStates, RegistrationStates
import config.keyboards as keyboards
import config.activity_dict as ad
from loader import dp

dict_of_activity = {}

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
            await call.message.answer('Отлично, перейдем к регистрации. Придумай логин.')
            await RegistrationStates.on_process_registration.set()

        if code == 3:
            await LoginState.on_start_menu.set()
            await call.message.answer(text="Что ты хочешь сделать?",
                                      reply_markup=keyboards.menu(), )


@dp.message_handler(state=RegistrationStates.on_process_registration)
async def end_registration(message: types.Message, state: FSMContext):
    print(message.text)
    await message.answer(f'Добро пожаловать,{message.text}!', reply_markup=keyboards.menu())
    await state.finish()


@dp.message_handler(commands=['phonenumber'])
async def phone(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить телефон",
                                        request_contact=True)
    keyboard.add(button_phone)
    await message.answer(message.conta,
                         reply_markup=keyboard)


@dp.message_handler(text='Создать мероприятие')
async def add_activity(message: types.Message):
    await CreateActivityStates.on_start_creating.set()
    await message.answer('Отлично! Узнаем немного о твоем будущем мероприятии:'
                         '\n1.Название мероприятия: ')


@dp.message_handler(state=CreateActivityStates.on_start_creating)
async def start(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    await message.answer('Теперь напишите дату в формате(дд.мм.гггг)')
    dict_of_activity['name'] = message.text
    await CreateActivityStates.on_date_of_activity.set()


@dp.message_handler(state=CreateActivityStates.on_date_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    await message.answer('Теперь напишите время проведения в формате(чч:мм)')
    dict_of_activity['date'] = message.text
    await CreateActivityStates.on_time_of_activity.set()


@dp.message_handler(state=CreateActivityStates.on_time_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    await message.answer('Теперь назначте место проведения')
    dict_of_activity['time'] = message.text
    await CreateActivityStates.on_place_of_activity.set()


@dp.message_handler(state=CreateActivityStates.on_place_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    await message.answer('Краткое описание мероприятия')
    dict_of_activity['place'] = message.text
    await CreateActivityStates.on_description_of_activity.set()


@dp.message_handler(state=CreateActivityStates.on_description_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    dict_of_activity['description'] = message.text
    print(dict_of_activity)
    await state.finish()


@dp.message_handler(text='Посмотреть мероприятия')
async def search_activity(message: types.Message):
    await message.answer('Вот мероприятия, которые могут тебя заинтересовать:)')
