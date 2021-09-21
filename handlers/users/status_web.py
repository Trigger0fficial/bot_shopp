from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp

price_product = 500
user_date = '27.09'
user_all_count = 18
user_lvl = {'x1': 0.2, 'x2': 0.35, 'x3': 0.5}
user_now_count = 4
user_pay = user_now_count * user_lvl['x3'] * price_product


def now_lvl():
    lvl_user = 0
    if user_all_count <= 5:
        lvl_user = 1
    elif 5 < user_all_count <= 15:
        lvl_user = 2
    elif user_all_count > 15:
        lvl_user = 3
    return lvl_user


lvl = now_lvl


# @dp.message_handler(Command('status'))
# async def show_status(message: Message):
#     if message.from_user.id == 745832259:
#         await message.answer(f'Твое имя - {message.from_user.full_name}'
#                              f'Твой id - {message.from_user.id}\n'
#                              f'Ты в команде находишься c {user_date}\n'
#                              f'Всего приглашенных пользователей - {user_all_count}\n'
#                              f'Твой уровень в TRIGGER - {user_lvl["x3"]}\n'
#                              f'Твоя выплата - {user_pay}')
#     else:
#         await message.answer('К сожалению ты не являешься партнером TRIGGER\n'
#                              'Ознакомься как стать Web master из пункта /menu')

