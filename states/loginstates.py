from aiogram.dispatcher.filters.state import StatesGroup, State


# здесь заданы состояния для хендлера выбора музыки

class LoginState(StatesGroup):
    on_start_menu = State()
    on_registation_menu = State()
    on_user_menu = State()
    get_back_menu = State()