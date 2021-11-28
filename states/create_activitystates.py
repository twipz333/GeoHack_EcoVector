from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateActivityStates(StatesGroup):
    on_start_creating = State()
    on_name_of_activity = State()
    on_date_of_activity = State()
    on_wait_esc_activity = State()
    on_time_of_activity = State()
    on_place_of_activity = State()
    on_description_of_activity = State()
    on_blank_creating = State()
    on_escape_creating = State()
    and_of_creating = State()