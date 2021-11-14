from aiogram.dispatcher.filters.state import StatesGroup, State


class State_coupon(StatesGroup):
    answer_user = State()


class State_chat_id(StatesGroup):
    answer_admin = State()
