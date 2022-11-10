from aiogram.dispatcher.filters.state import State, StatesGroup


class StartState(StatesGroup):
    langState = State()
    phoneState = State()
    nameState = State()


class AloqaState(StatesGroup):
    aloqaState = State()