from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep

from handlers.users.status_web import user_date, user_all_count, user_lvl, user_pay
from keyboards.default import menu
from keyboards.default.menu import choice
from loader import dp
from states.verification_coupon import State_coupon

all_web = [745832259, 123456789]
lvl_web = {'x1': 0.2, 'x2': 0.35, 'x5': 0.5}


class Web_master:
    def __init__(self, user_id, user_name, user_date, user_all_count_invited=0, user_lvl='x1'):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date = user_date
        self.user_all_count_invited = user_all_count_invited
        self.user_count_invited = 0
        self.user_lvl = {'x1': 0.2, 'x2': 0.35, 'x5': 0.5}
        self.user_pay = 0
        self.lvl = user_lvl

    def profit_web(self, lvl):
        self.user_count_invited += 1
        self.user_all_count_invited += 1
        self.user_pay += lvl * 500

    def paid_web(self):
        self.user_pay = 0
        self.user_count_invited = 0

    def __str__(self):
        return f'--------------------------------------------------\n' \
               f'Name_web: {self.user_name}\nId_web: {self.user_id}\n' \
               f'Date_web: {self.user_date}\nLvl_web: {self.user_lvl}\n' \
               f'Total_user: {self.user_all_count_invited}  Now_user: {self.user_count_invited}\n' \
               f'Pay_web: {self.user_pay}'




list_web_master = [
    Web_master(user_id=1111111, user_name='Vladislav', user_date='22.09'),
    Web_master(user_id=222222, user_name='Sergey', user_date='22.09'),
    Web_master(user_id=0000000, user_name='Test', user_date='21.09'),
    Web_master(user_id=745832259, user_name='Dima', user_date='21.09'),
    Web_master(user_id=1847339325, user_name='Sasha', user_date='21.09')
]



def activity_web_master():
    list_web_master[2].profit_web(lvl=lvl_web['x1'])
    list_web_master[2].profit_web(lvl=lvl_web['x1'])
    list_web_master[4].profit_web(lvl=lvl_web['x5'])
    list_web_master[4].profit_web(lvl=lvl_web['x5'])
    list_web_master[4].profit_web(lvl=lvl_web['x5'])

    for web in list_web_master:
        print(web.__str__())


activity_web_master()


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Что ты хочешь сделать?',
                         reply_markup=menu)


@dp.message_handler(Text(equals=['Купить FORECAST', 'Стать Web master',
                                 'INFO']))
async def get_food(message: Message):
    if message.text == 'INFO':
        await message.answer('Переходи по ссылке, ознакомься с каналом\n'
                             'https://t.me/joinchat/sCVGkTC9ojs4YTMy',
                             reply_markup=ReplyKeyboardRemove())

    elif message.text == 'Купить FORECAST':
        await message.answer('ℹ️ Поговорим о продукте который предоставляет наш проект❗\n'
                             'Наш продукт представляет собой, математический\n'
                             'анализатор событий. Тоесть, это математическая программа,\n'
                             'которая позволяет пользователю делать ставки на спорт \n'
                             'без риска уйти в минус❗️\n\n'
                             'Программа учитывает коэффициент 2 - ух ставок,\n'
                             'рассчитывает суммы которые вам нужно поставить на ту,\n'
                             'или иную команду, исходя из вашего депозита. Таким образом,\n'
                             'позволяя не рисковать вашими средствами.\n\n'
                             'Стоимость нашего продукта - 600₽. Но его можно приобрести\n'
                             'со скидкой в 15% предварительно введя скидочный КУПОН ✅\n\n'
                             'Так же у нас имеется VIP чат, в котором мы выкладываем \n'
                             'прогнозы на матчи.\n'
                             'Стоимость данного чата - 250₽ ✅',
                             reply_markup=choice)

    elif message.text == 'Стать Web master':
        await message.answer(f'{message.from_user.full_name}, '
                             f'поздравляю тебя❗️ Ты решил стать Вебмастером проекта TRIGGER.\n'
                             f'Чтобы получить доступ к реферальной программе проекта,\n'
                             f'Напиши фразу "Хочу стать Вебмастером" и пришли мне кодовое слово\n'
                             f'На аккаунт администрации @keepeero\n'
                             f'Твое кодовое слово - {message.from_user.id}\n'
                             f'В течении 10-15 мин, администрация проекта свяжется с тобой ✅',
                             reply_markup=ReplyKeyboardRemove())

    else:
        await message.answer('Такого варианта нет, повторите попытку!')


@dp.message_handler(Text(equals=['Купить 600р']))
async def buy_product(message: Message):
    if message.text == 'Купить 600р':
        await message.answer(f'Ты выбрал к покупке продукт FORECAST.\n\n'
                             f'Чтобы оплатить продукт, тебе необходимо \n'
                             f'воспользоваться переводом средств на карту:\n'
                             f'4276 5209 6316 4385 ✅\n\n'
                             f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                             f'Необходимо прикрепить комментарий к платежу:\n'
                             f'{ message.from_user.id}\nИ указать соотвествующую сумму выбранного вами \nпакета❗️\n'
                             f'ℹ️В ином случае твоя покупка будет считаться\n'
                             f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=['Использовать купон - 500р']), state=None)
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
        comment_user = str(user) + 'afc' + str(message.from_user.id)
        await message.answer('Твой купон действительный!\n'
                             f'Ты выбрал к покупке продукт FORECAST.\n\n'
                             f'Чтобы оплатить продукт, тебе необходимо \n'
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
        await message.answer('К сожалению, такого купона нет!')
        await state.finish()


@dp.message_handler(Command('status'))
async def show_status(message: Message):
    for web in list_web_master:
        if message.from_user.id == web.user_id:
            await message.answer(f'Твое имя - {message.from_user.full_name}\n'
                                 f'Твой id - {message.from_user.id}\n'
                                 f'Ты в команде c {web.user_date}\n'
                                 f'Всего приглашенных пользователей - {web.user_all_count_invited}\n'
                                 f'Неоплаченных пользователей - {web.user_count_invited}\n'
                                 f'Твой уровень в TRIGGER - {user_lvl["x3"]}\n'
                                 f'Твоя выплата - {web.user_pay}')
            break
    else:
        await message.answer('К сожалению ты не являешься партнером TRIGGER\n'
                             'Ознакомься как стать Web master из пункта /menu')


@dp.message_handler(Text(equals=['VIP канал - 250р']))
async def show_vip_channel(message: Message):
    await message.answer(f'Ты выбрал к покупке VIP чат\n\n'
                         f'Чтобы оплатить продукт, тебе необходимо \n'
                         f'воспользоваться переводом средств на карту:\n'
                         f'4276 5209 6316 4385 ✅\n\n'
                         f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                         f'Необходимо прикрепить комментарий к платежу:\n'
                         f'{message.from_user.id}\n'
                         f'ℹ️В ином случае твоя покупка будет считаться\n'
                         f'незафиксированной ℹ️',
                         reply_markup=ReplyKeyboardRemove())