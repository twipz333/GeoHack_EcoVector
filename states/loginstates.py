from aiogram.dispatcher.filters.state import StatesGroup, State


class LoginState(StatesGroup):
    on_start_menu = State()
    on_registation_menu = State()
    on_user_menu = State()
    get_back_menu = State()