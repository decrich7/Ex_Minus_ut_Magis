from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    enter_name = State()
    group = State()
