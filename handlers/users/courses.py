from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep

from handlers.users.menu import all_web
from keyboards.default import menu
from keyboards.default.menu import choice, info, choice_courses, select_package, buy_course, show_courses
from loader import dp
from states.verification_coupon import State_coupon


PY_PRO = 2600
PY_START = 2000
JS_BASICS = 1800
PM_12 = 3700
PM_23 = 3000
PM_31 = 3500
name_course_buy = 0


@dp.message_handler(Text(equals=['Курсы 🎓']))
async def show_course(message: Message):
    await message.answer('Описание зачем trigger это делает и что оно вам даст', reply_markup=show_courses)


@dp.message_handler(Text(equals='Информация о курсах'))
async def inf_courses(message: Message):
    await message.answer('Страница о всех курсах')


@dp.message_handler(Text(equals='Купить курсы'))
async def courses(message: Message):
    await message.answer('Что ты хочешь приобрести?', reply_markup=choice_courses)



@dp.message_handler(Text(equals=['Py start', 'Py pro', 'Js basics', 'Выбрать пакет']))
async def select_courses(message: Message):
    global name_course_buy
    if message.text == 'Py start':
        name_course_buy = PY_START
    elif message.text == 'Py pro':
        name_course_buy = PY_PRO
    elif message.text == 'Js basics':
        name_course_buy = JS_BASICS
    elif message.text == 'Выбрать пакет':
        await message.answer('Рассказать что вы можете взять курс пакетом и на этом сэкономить',
                             reply_markup=select_package)
        return

    await message.answer(f'Курс {message.text} стоит {name_course_buy * 1.2}р\nЕсли вы планируете брать с купоном, '
                         f'то его цена составляет {name_course_buy}р', reply_markup=buy_course)



@dp.message_handler(Text(equals=['Py start + Py pro', 'Py pro + Js basics', 'Py start + Js basics']))
async def buy_package(message: Message):
    global name_course_buy
    if message.text == 'Py start + Py pro':
        name_course_buy = PM_12

    elif message.text == 'Py pro + Js basics':
        name_course_buy = PM_31

    elif message.text == 'Py start + Js basics':
        name_course_buy = PM_23


    await message.answer(
        f"Цена пакета \"{message.text}\" составляет - {name_course_buy * 1.2}р\nС использованием купона - {name_course_buy}р",
        reply_markup=buy_course)


@dp.message_handler(Text(equals=['Использовать купон']), state=None)
async def buy_product_web(message: Message):
    await message.answer('Введите купон', reply_markup=ReplyKeyboardRemove())
    await State_coupon.answer_user.set()


@dp.message_handler(state=State_coupon.answer_user)
async def get_user_coupon(message: Message, state: FSMContext):
    answer_user = message.text
    await state.update_data(answer=answer_user)
    data = await state.get_data()
    user = data.get('answer')
    if user in str(all_web):
        comment_user = str(user) + 'Afc' + str(message.from_user.username)
        await message.answer('Твой купон действительный!\n'
                             f'Чтобы оплатить , тебе необходимо \n'
                             f'воспользоваться переводом средств на карту:\n'
                             f'4276 5209 6316 4385 ✅\n\n'
                             f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                             f'Необходимо прикрепить комментарий к платежу:\n'
                             f'{comment_user}\nИ указать соотвествующую сумму выбранного вами \nпакета❗️\n'
                             f'ℹ️В ином случае твоя покупка будет считаться\n'
                             f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove()
                             )
        await state.finish()
    else:
        await message.answer('К сожалению, такого купона нет!', reply_markup=choice)
        await state.finish()


@dp.message_handler(Text(equals='Купить'))
async def buy_courses(message: Message):
    comment = message.from_user.username + "2e" + str(message.from_user.id)
    await message.answer(f'Чтобы оплатить курс, тебе необходимо \n'
                         f'воспользоваться переводом средств на карту:\n'
                         f'4276 5209 6316 4385 ✅\n\n'
                         f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                         f'Необходимо прикрепить комментарий к платежу:\n'
                         f'{comment}\nИ указать соотвествующую сумму выбранного вами \nкурса/пакета курса❗️\n'
                         f'ℹ️В ином случае твоя покупка будет считаться\n'
                         f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove())