from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import utils.reqtest as get


def initialization(message):
    keyboard = InlineKeyboardMarkup()
    tg_uid = get.get_user_add('tg_uid')
    menu_1 = InlineKeyboardButton(text='Помощь', callback_data="menu_1")
    flag = False
    for i in tg_uid:
        if int(i) != message.chat.id:
            flag = False
        else:
            flag = True
            break

    if not flag:
        menu_2 = InlineKeyboardButton(text='Регистрация', callback_data="menu_2")
        keyboard.add(menu_1, menu_2)
    else:
        menu_3 = InlineKeyboardButton(text='Главное меню', callback_data="menu_3")
        keyboard.add(menu_1, menu_3)
    return keyboard


def escape_button():
    escape_button = KeyboardButton("Отменить создание")
    escape_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(escape_button)
    return escape_markup


def menu():
    add_activity = KeyboardButton("Создать мероприятие")
    search_activity = KeyboardButton("Посмотреть мероприятия")
    add_comment = KeyboardButton("Оставить отзывы")
    activity_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        add_activity).add(search_activity).add(add_comment)

    return activity_markup

