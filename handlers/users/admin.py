from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep

from handlers.users.status_web import user_date, user_all_count, user_lvl, user_pay
from keyboards.default.admin import admin_courses
from keyboards.default.menu import choice, info, admin_btn, choice_courses, select_package
from loader import dp, bot
# from states.verification_coupon import State_coupon, State_chat_id
from states.verification_coupon import State_chat_id

# from handlers.users.menu import counter_web, counter_info_web
# from handlers.users.courses import counter_buy, counter_courses, counter_coupon


# counter_web = 0
# counter_info_web = 0
# counter_buy = 0
# counter_courses = 0
# counter_coupon = 0

list_admin = [745832259, 869546657]
act_admin = False
send_product = ''
chat_id = ''



@dp.message_handler(Command('admin'))
async def show_admin_btn(message: Message):
    if message.from_user.id in list_admin:
        await message.answer('Вы вошли в панель администрации', reply_markup=admin_btn)
    else:
        await message.answer('Вы не являетесь админом TriggerShop!')


@dp.message_handler(Text(equals='Отправить курс 💎'))
async def send_courses(message: Message):
    if message.from_user.id in list_admin:
        await message.answer('❗Выбери курс❗', reply_markup=admin_courses)
    else:
        await message.answer('Вы не являетесь админом TriggerShop!')


@dp.message_handler(Text(equals=['Py start ❗', 'Py pro ❗', 'C_UNITY ❗', '❗Py start + Py pro❗',
                                 '❗Py pro + C_UNITY❗', '❗Py start + C_UNITY❗']))
async def choose_course(message: Message):
    global send_product
    if message.from_user.id in list_admin:
        if message.text == 'Py start ❗':
            send_product = 'Курс Py start ❗ отправлен'
        elif message.text == 'Py pro ❗':
            send_product = 'Курс Py pro ❗ отправлен'
        elif message.text == 'C_UNITY ❗':
            send_product = 'Курс C_UNITY ❗ отправлен'
        elif message.text == '❗Py start + Py pro❗':
            send_product = 'Пакет ❗Py start + Py pro❗ отправлен'
        elif message.text == '❗Py pro + C_UNITY❗':
            send_product = 'Пакет ❗Py pro + C_UNITY❗ отправлен'
        elif message.text == '❗Py start + C_UNITY❗':
            send_product = 'Пакет ❗Py start + C_UNITY❗ отправлен'
    await message.answer('Введи id чата, кому нужно отправить курс/пакет', reply_markup=ReplyKeyboardRemove())
    await State_chat_id.answer_admin.set()

@dp.message_handler(state=State_chat_id.answer_admin)
async def get_chat_id(message: Message, state: FSMContext):
    global chat_id
    user_chat_id = message.text
    await state.update_data(answer=user_chat_id)
    data = await state.get_data()
    chat_id = data.get('answer')
    await state.finish()
    await message.answer(text='Сообщение для админа')

    await bot.send_message(text=send_product, chat_id=chat_id)


# @dp.message_handler(Text(equals='Статистика 🔎'))
# async def show_statics(message: Message):
#     await message.answer(f'Статистика посещения:\n'
#                          f'Переходы на курсы: {counter_courses}\n'
#                          f'Переходы на info_web: {counter_info_web}\n'
#                          f'Переходы на WEB: {counter_web}\n'
#                          f'Переходы на покупку: {counter_buy}\n'
#                          f'Переходы на покупку с купоном {counter_coupon}')

























