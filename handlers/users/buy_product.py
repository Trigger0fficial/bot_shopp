import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choise_data import choice_price
from loader import dp


@dp.message_handler(Command('buy'))
async def show_price(message: Message):
    await message.answer(text='Описание продукта', reply_markup=choice_price)



# @dp.callback_query_handlers(text_contains='buy:price:500')
# async def buy_product_500(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     callback_data = call.data
#     logging.info('call - {}'.format(callback_data))
#     await call.message.answer('Поздравляю! Вы выбрали покупку за 500р')

# @dp.callback_query_handlers(text='cancel')
# async def cancel_buy(call: CallbackQuery):
#     await call.answer('Вы отменили покупку!', show_alert=True)
#     # await call.message.edit_reply_markup()
