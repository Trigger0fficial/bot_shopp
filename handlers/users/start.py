from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('{}, тебя привествует TriggerShop!'.format
                         (message.from_user.full_name))
    await message.answer('TRIGGER_SHOP, это онлайн магазин проекта TRIGGER.\n'
                         'Он предоставляет пользователю список продуктов и \n'
                         'предложений нашего проекта.\n\n'
                         'Что ознакомиться со всеми командами бота \n'
                         'нажмите /help ℹ️\n\n'
                         'Чтобы ознакомиться с предложениями нажмите /menu,\n'
                         'перед вами откроются 3 кнопки♻️\n'
                         '1) - Если вы хотите купить продукт, нажмите на кнопку\n'
                         '"Приобрести" ℹ️\n'
                         '2) - Если вы хотите стать Вебмастером проекта, ❗️сначала \n'
                         'ознакомьтесь с информационным каналом❗️\n'
                         'нажав кнопку INFO WEB, после того, как вы изучили \n'
                         'информацию о деятельности Вебмастера, и решили стать \n'
                         'нашим рефералом, нажми на кнопку "Стать WEB" ℹ️ \n\n'
                         '❗Пользуясь ботом TRIGGER_SHOP, вы принимаете\n'
                         'пользовательское соглашение, с которым вы можете\n'
                         'ознакомиться нажав /agreement 👤❗️\n\n'
                         'С уважение TRIGGER_TEAMS ✅')


