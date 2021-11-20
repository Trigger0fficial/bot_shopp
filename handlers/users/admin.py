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



list_admin = [745832259, 869546657]
send_product = ''
courses = ''
courses_gif = ''
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
    global courses
    global courses_gif
    if message.from_user.id in list_admin:
        if message.text == 'Py start ❗':
            send_product = 'Привет дорогой друг❗\n' \
                           'Ты приобрёл курс по программированию PY_START 🐍✅\n' \
                           'Желаем удачи в прохождении данного курса и надеемся\n' \
                           'увидеть тебя в нашей команде 👥🔥\n\n' \
                           'PY_START ‼️(https://t.me/joinchat/Lzb6Nm_5Cqo5NWUy)‼\n\n' \
                           'Возникли вопросы по курсу?\n' \
                           'Напиши НАМ @keepeero\n\n' \
                           'С уважением TRIGGER TEAMS ❗'
            courses = "Py start"

        elif message.text == 'Py pro ❗':
            send_product = 'В разработке'

        elif message.text == 'C_UNITY ❗':
            send_product = 'Привет дорогой друг❗\n' \
                           'Ты приобрёл курс по программированию C_UNITY 🐍✅\n' \
                           'Желаем удачи в прохождении данного курса и надеемся\n' \
                           'увидеть тебя в нашей команде 👥🔥\n\n' \
                           'C_UNITY ‼️(https://t.me/joinchat/hNumn91DG6dhNjMy)‼️‼\n\n' \
                           'Возникли вопросы по курсу?\n' \
                           'Напиши НАМ @keepeero\n\n' \
                           'С уважением TRIGGER TEAMS ❗'
            courses = 'C_UNITY'

        elif message.text == '❗Py start + Py pro❗':
            send_product = 'В разработке'

        elif message.text == '❗Py pro + C_UNITY❗':
            send_product = 'В разработке'


        elif message.text == '❗Py start + C_UNITY❗':
            send_product = 'Привет дорогой друг❗\n' \
                           'Ты приобрёл пакет курсов по программированию 🐍✅ PY_START и C_UNITY🐍✅\n' \
                           'Желаем удачи в прохождении данного курса и надеемся\n' \
                           'увидеть тебя в нашей команде 👥🔥\n\n' \
                           'C_UNITY ‼️(https://t.me/joinchat/hNumn91DG6dhNjMy)‼️‼\n' \
                           'PY_START ‼️(https://t.me/joinchat/Lzb6Nm_5Cqo5NWUy)‼\n\n' \
                           'Возникли вопросы по курсу?\n' \
                           'Напиши НАМ @keepeero\n\n' \
                           'С уважением TRIGGER TEAMS ❗'
            courses = 'Py start + C_UNITY'

        if courses == 'Py start':
            courses_gif = 'Gif/py_start-gif.mp4'
        elif courses == 'C_UNITY':
            courses_gif = 'Gif/c_unity-gif.mp4'
        elif courses == 'Py start + C_UNITY':
            courses_gif = 'Gif/py_start-c_unity-gif.mp4'
        else:
            courses_gif = "None"


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
    try:
        open_gif = open(courses_gif, "rb")
        await bot.send_video(chat_id=chat_id, video=open_gif)
        await bot.send_message(text=send_product, chat_id=chat_id)
        await message.answer('Сообщение было успешно доставлено')
    except:
        await message.answer('Сообщение не было доставлено')



























