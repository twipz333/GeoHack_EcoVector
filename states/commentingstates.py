from aiogram.dispatcher.filters.state import StatesGroup, State

class CommentingStates(StatesGroup):
    on_start_commenting = State()
