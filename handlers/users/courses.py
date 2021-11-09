from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep


from aiogram.types.base import InputFile

from handlers.users.menu import all_web
from keyboards.default import menu
from keyboards.default.menu import choice, info, choice_courses, select_package, buy_course, show_courses
from loader import dp
from states.verification_coupon import State_coupon

PY_PRO = 2600
PY_START = 2500
C_UNITY = 3000
PM_12 = 3700
PM_23 = 4300
PM_31 = 3500
name_course_buy = 0
answer_description = ''
answer_gif = ''
courses_gif = open("Gif/courses.mp4", "rb")



@dp.message_handler(Text(equals=['Курсы 🎓']))
async def show_course(message: Message):
    # await message.answer_video(video=courses_gif)

    await message.answer('❗Новый проект от TRIGGER_COURSES предлагает Вам несколько курсов на разные сферы IT❗\n'
                         'Каждый курс включает в себя до 20 видео лекций, десятки практических задач разного уровня '
                         'сложности, личного наставника и возможность купить сразу пакет курсов и получить за это '
                         'хорошую скидку\n\n'
                         'Компания TRIGGER начала набор штата программистов, для этого мы Вам представляем курсы от TRIGGER\n'
                         'При успешном прохождении курса у вас появляется отличная возможность начать\n'
                         'зарабатывать, благодаря digital компании TRIGGER.\n'
                         'Для ознакомления более детальной информации\n'
                         'мы Вам сначала предлагаем посетить страницу\n'
                         '"Информация о курсах📌"', reply_markup=show_courses)



@dp.message_handler(Text(equals='❓Информация о курсах❓'))
async def inf_courses(message: Message):
    await message.answer('https://t.me/joinchat/MLTXX7PJEXZiZDAy')


@dp.message_handler(Text(equals='Купить курсы✅'))
async def courses(message: Message):
    await message.answer('Что ты хочешь приобрести?', reply_markup=choice_courses)


@dp.message_handler(Text(equals=['Py start 🔥', 'Py pro ⛔', 'C_UNITY 💥', 'Выбрать пакет 🔜']))
async def select_courses(message: Message):
    global name_course_buy
    global answer_description
    global answer_gif

    if message.text == 'Py start 🔥':
        name_course_buy = PY_START
        answer_gif = open("Gif/py_start-gif.mp4", "rb")
        answer_description = '🔥PY_START🔥\n' \
                             'Приветствуем дорогой друг! Ты заинтересовался курсом по\n' \
                             'программированию 🔥PY_START🔥❗. В данном курсе, ты получишь' \
                             'основные знания программирования на языке PYTHON.\n' \
                             '❗В курс PY_START входят 10 лекционных занятий (видео уроки) и' \
                             '10 основных задач ➕ 4-10 практических заданий к каждому уроку❗\n\n' \
                             'У тебя есть возможность получить данный курс с\n' \
                             '"кураторством". Куратор будет отвечать на все твои вопросы и\n' \
                             'помогать с прохождением практической части!\n' \
                             'Если вы не приобрели курс с "кураторством" в начале, то в \n' \
                             'течении прохождения курса вы можете решить этот вопрос\n' \
                             'написав нам @keepeero.\n\n' \
                             '❗Остались вопросы? Тогда напиши нам - @keepeero или \n' \
                             'посмотри инфо (https://t.me/joinchat/MLTXX7PJEXZiZDAy) канал❗'


    elif message.text == 'Py pro ⛔':
        name_course_buy = PY_PRO
        await message.answer('❗Курс находится в разработке❗')
        return
    elif message.text == 'C_UNITY 💥':
        name_course_buy = C_UNITY
        answer_gif = open("Gif/c_unity-gif.mp4", "rb")
        answer_description = '💥C_UNITY💥\n' \
                             'Приветствуем дорогой друг! Ты заинтересовался курсом по\n' \
                             'программированию 💥C_UNITY💥. В данном курсе, ты получишь' \
                             'основные знания по разработке игр для платформы Андроид на движке UNITY.\n' \
                             'В курс 💥C_UNITY💥 входят 15 видеоуроков, в которых от А до Я затрагиваются все ' \
                             'основные аспекты в создании любой мобильной игры!\n\n' \
                             'У тебя есть возможность получить данный курс с\n' \
                             '"кураторством". Куратор будет отвечать на все твои вопросы и\n' \
                             'предоставит доступ к дополнительной практической части!\n' \
                             'Если вы не приобрели курс с "кураторством" в начале, то в \n' \
                             'течении прохождения курса вы можете решить этот вопрос\n' \
                             'написав нам @keepeero.\n' \
                             '❗Остались вопросы? Тогда напиши нам - @keepeero или \n' \
                             'посмотри инфо (https://t.me/joinchat/MLTXX7PJEXZiZDAy) канал❗'

    elif message.text == 'Выбрать пакет 🔜':
        await message.answer('Приобретая пакет ты получаешь 20% скидку с каждого курса,который входит в твой пакет ➕ '
                             '50% скидку на кураторство одного из курсов',
                             reply_markup=select_package)
        return




    await message.answer_video(video=answer_gif)
    await message.answer(f'{answer_description}', reply_markup=buy_course)


@dp.message_handler(Text(equals=['⛔Py start + Py pro⛔', '⛔Py pro + C_UNITY⛔', '🔥Py start + C_UNITY💥']))
async def buy_package(message: Message):
    global name_course_buy
    global answer_gif
    global answer_description
    if message.text == '⛔Py start + Py pro⛔':
        name_course_buy = PM_12
        await message.answer('❗Пакет находится в разработке❗')
        return

    elif message.text == '⛔Py pro + C_UNITY⛔':
        name_course_buy = PM_31
        await message.answer('❗Пакет находится в разработке❗')
        return

    elif message.text == '🔥Py start + C_UNITY💥':
        name_course_buy = PM_23
        answer_gif = open("Gif/py_start-c_unity-gif.mp4", "rb")
        answer_description = '💥🔥Py start + C_UNITY💥🔥\n' \
                             'Приветствуем дорогой друг! Ты заинтересовался пакетом с\n' \
                             'курсами по программированию PY_START + C_UNITY. В данном\n' \
                             'пакете ты получишь оба курса, благодаря которым, ты\n' \
                             'научишься программировать на языке PYTHON, и писать игры\n' \
                             'на движке UNITY. В курс PY_START входят 10 лекционных\n' \
                             'занятий (видеоуроки), так же 10 основных заданий и 4-10 дополнительных ' \
                             'практический задач в каждом уроке!\n' \
                             'В курс C_UNITY входят 15 видео уроков и 3-7 практических задач в каждом уроке! \n\n' \
                             '‼️Самое "вкусное", что ты получишь - это не только два \n' \
                             'классных курса по программированию, но и хорошая скидка\n' \
                             'на данный пакет‼\n\n' \
                             'У тебя есть возможность получить данный курс с\n' \
                             '"кураторством". Куратор будет отвечать на все твои вопросы и\n' \
                             'предоставит доступ к дополнительной практической части!\n' \
                             'Если вы не приобрели курс с "кураторством" в начале, то в \n' \
                             'течении прохождения курса вы можете решить этот вопрос\n' \
                             'написав нам @keepeero.\n' \
                             'Остались вопросы? Тогда напиши нам - @keepeero или \n' \
                             'посмотри https://t.me/joinchat/MLTXX7PJEXZiZDAy канал❗'


    await message.answer_video(video=answer_gif)
    await message.answer(answer_description,
                         reply_markup=buy_course)


@dp.message_handler(Text(equals=['Использовать купон 💣']), state=None)
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
        comment_user = str(user) + 'Afc' + str(message.from_user.id)
        await message.answer('Твой купон действительный!\n'
                             f'Чтобы оплатить , тебе необходимо \n'
                             f'воспользоваться переводом средств на карту:\n'
                             f'4276 5209 6316 4385 ✅\n'
                             f'Стоимость твоего курса составляет - {name_course_buy}р💥\n\n'
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


@dp.message_handler(Text(equals='Купить ✅'))
async def buy_courses(message: Message):
    comment = message.from_user.username + "2e" + str(message.from_user.id)
    await message.answer(f'Чтобы оплатить курс, тебе необходимо \n'
                         f'воспользоваться переводом средств на карту:\n'
                         f'4276 5209 6316 4385 ✅\n'
                         f'Стоимость твоего курса составляет - {name_course_buy * 1.2}р💥\n\n'
                         f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                         f'Необходимо прикрепить комментарий к платежу:\n'
                         f'{comment}\nИ указать соотвествующую сумму выбранного вами \nкурса/пакета курса❗️\n'
                         f'ℹ️В ином случае твоя покупка будет считаться\n'
                         f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove())
