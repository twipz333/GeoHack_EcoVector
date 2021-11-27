from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def initialization(message):
    print(message.chat.id)
    keyboard = InlineKeyboardMarkup()
    menu_1 = InlineKeyboardButton(text='Помощь', callback_data="menu_1")
    if message.chat.id == 443808849:  # проверка регистрации
        menu_2 = InlineKeyboardButton(text='Регистрация', callback_data="menu_2")
        keyboard.add(menu_1, menu_2)
    else:
        menu_3 = InlineKeyboardButton(text='Главное меню', callback_data="menu_3")
        keyboard.add(menu_1, menu_3)
    return keyboard


def menu():
    add_activity = KeyboardButton("Создать мероприятие")
    search_activity = KeyboardButton("Посмотреть мероприятия")
    activity_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        add_activity).add(search_activity)

    return activity_markup
