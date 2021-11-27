from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states import LoginState, CreateActivityStates, RegistrationStates, CommentingStates
import config.keyboards as keyboards
import config.activity_dict as ad
import utils.reqtest as post
import random
from loader import dp

dict_of_activity = {}
dict_of_user = {}


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
            await call.message.answer(text="Что ты хочешь сделать?",
                                      reply_markup=keyboards.menu(), )


@dp.message_handler(state=RegistrationStates.on_process_registration)
async def end_registration(message: types.Message, state: FSMContext):
    print('1', message.text)
    dict_of_user['username'] = message.text
    dict_of_user['tg_uid'] = message.chat.id
    print('2', message.chat.id)
    post.post_user_add(uid=f'1231231', tg_uid=f'{message.chat.id}', username=f'{message.text}')
    await message.answer(f'Добро пожаловать,{message.text}!', reply_markup=keyboards.menu())
    await state.finish()


@dp.message_handler(text='Оставить отзывы')
async def add_comment(message: types.Message):
    await CommentingStates.on_start_commenting.set()
    await message.answer('Тут хранятся мероприятия, на которые ты можешь оставить отзыв')


@dp.message_handler(text='Создать мероприятие')
async def add_activity(message: types.Message):
    await CreateActivityStates.on_start_creating.set()
    await message.answer('Отлично! Узнаем немного о твоем будущем мероприятии:'
                         '\n1.Название мероприятия: ', reply_markup=keyboards.escape_button())


@dp.message_handler(state=CreateActivityStates.on_start_creating)
async def start(message: types.Message, state: FSMContext):
    await CreateActivityStates.on_date_of_activity.set()
    await ad.mk_dict(message, state)
    await message.answer('Теперь напишите дату в формате(дд.мм.гггг)', reply_markup=keyboards.escape_button())
    dict_of_activity['name'] = message.text
    if message.text == 'Отменить создание':
        await state.finish()

@dp.message_handler(state=CreateActivityStates.on_date_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await CreateActivityStates.on_time_of_activity.set()
    await ad.mk_dict(message, state)
    await message.answer('Теперь напишите время проведения в формате(чч:мм)', reply_markup=keyboards.escape_button())
    dict_of_activity['date'] = message.text
    if message.text == 'Отменить создание':
        await state.finish()


@dp.message_handler(state=CreateActivityStates.on_time_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await CreateActivityStates.on_place_of_activity.set()
    await ad.mk_dict(message, state)
    await message.answer('Теперь назначте место проведения', reply_markup=keyboards.escape_button())
    dict_of_activity['time'] = message.text
    if message.text == 'Отменить создание':
        await state.finish()

@dp.message_handler(state=CreateActivityStates.on_place_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await CreateActivityStates.on_description_of_activity.set()
    await ad.mk_dict(message, state)
    await message.answer('Краткое описание мероприятия', reply_markup=keyboards.escape_button())
    dict_of_activity['place'] = message.text
    if message.text == 'Отменить создание':
        await state.finish()

@dp.message_handler(state=CreateActivityStates.on_description_of_activity)
async def set_activity_name(message: types.Message, state: FSMContext):
    await ad.mk_dict(message, state)
    dict_of_activity['description'] = message.text
    print(dict_of_activity)
    await state.finish()
    if message.text == 'Отменить создание':
        await state.finish()

@dp.message_handler(text='Отменить создание')
async def escape_creation(message: types.Message, state: FSMContext):
    await message.answer(f'Создание отменено'
                         f'\nЧем могу помочь?', reply_markup=keyboards.initialization(message))
    await state.finish()

@dp.message_handler(text='Посмотреть мероприятия')
async def search_activity(message: types.Message):
    await message.answer('Вот мероприятия, которые могут тебя заинтересовать:)')
