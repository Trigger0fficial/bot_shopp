from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline import callback_data
from keyboards.inline.callback_data import buy_callback

# choice_price = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Купить 600р', callback_data=buy_callback.new(
#                 price=600
#             )),
#             InlineKeyboardButton(text='Воспользоваться купоном\nКупить 500р', callback_data=buy_callback.new(
#                 price=500
#             )),
#             InlineKeyboardButton(text='Приватный чат - 200р', callback_data=buy_callback.new(
#                 price=200
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='Вернуться назад', callback_data='cancel')
#         ]
#     ]
# )

choice_price = InlineKeyboardMarkup(row_width=3)
buy_user = InlineKeyboardButton(text='Купить 600р', callback_data='buy:600')
choice_price.insert(buy_user)

buy_web_user = InlineKeyboardButton('Купить 500р', callback_data=buy_callback.new(
    price="500"
))
choice_price.insert(buy_web_user)

buy_vip = InlineKeyboardButton(text='Купить VIP', callback_data="buy:250")
choice_price.insert(buy_vip)