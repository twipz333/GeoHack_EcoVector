from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateActivityStates(StatesGroup):
    on_start_creating = State()
    on_blank_creating = State()
    and_of_creating = State()