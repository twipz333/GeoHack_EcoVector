from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    on_start_registration = State()
    on_process_registration = State()
    