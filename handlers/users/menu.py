from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep

from handlers.users.status_web import user_date, user_all_count, user_lvl, user_pay
from keyboards.default import menu
from keyboards.default.menu import choice, info
from loader import dp
from states.verification_coupon import State_coupon

all_web = [453881767, 679823483, 1751888736, 745832259, 720438045, 1234, 987]
lvl_web = {'x1': 0.2, 'x2': 0.35, 'x3': 0.5}


class Web_master:
    def __init__(self, user_id, user_name, user_date, user_all_count_invited=0, user_lvl='x1', render_lvl='x1'):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date = user_date
        self.user_all_count_invited = user_all_count_invited
        self.user_count_invited = 0
        self.render_lvl = render_lvl
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
               f'Date_web: {self.user_date}\nLvl_web: {self.render_lvl}\n' \
               f'Total_user: {self.user_all_count_invited}  Now_user: {self.user_count_invited}\n' \
               f'Pay_web: {self.user_pay}'




list_web_master = [
    Web_master(user_id=453881767, user_name='Anton', user_date='22.09', render_lvl='x1'),
    Web_master(user_id=679823483, user_name='Vladislav', user_date='22.09', render_lvl='x3'),
    Web_master(user_id=1751888736, user_name='Sergey', user_date='22.09', render_lvl='x3'),
    Web_master(user_id=745832259, user_name='Dima', user_date='21.09', render_lvl='x3'),
    Web_master(user_id=720438045, user_name='Katya', user_date='22.09', render_lvl='x1'),
    Web_master(user_id=1234, user_name='Valera',user_date='23.09', render_lvl='x1'),
    Web_master(user_id=987, user_name='Advin', user_date='23.09', render_lvl='x3'),


]



def activity_web_master():
    list_web_master[3].profit_web(lvl=lvl_web['x1']),
    list_web_master[3].profit_web(lvl=lvl_web['x3']),
    list_web_master[3].paid_web(),
    list_web_master[5].profit_web(lvl=lvl_web['x1']),
    list_web_master[5].paid_web(),
    list_web_master[6].profit_web(lvl=lvl_web['x3']),
    list_web_master[6].profit_web(lvl=lvl_web['x3']),
    list_web_master[6].paid_web()

    for web in list_web_master:
        print(web.__str__())


def admin_trigger():
    total_pay = 0
    total_web = 0
    total_count_invited = 0
    for web in list_web_master:
        total_pay += web.user_pay
        total_count_invited += web.user_all_count_invited
        total_web += 1


    print(f'\n--------Admin---------'
          f'\nTotal web: {total_web}\n'
          f'All invited: {total_count_invited}\n'
          f'Pay total: {total_web}')
    activity_web_master()


admin_trigger()


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Что ты хочешь сделать?',
                         reply_markup=menu)


@dp.message_handler(Text(equals=['Купить FORECAST ✅', 'Стать Web master🔥',
                                 'INFO WEB⚠',]))
async def get_food(message: Message):
    if message.text == 'INFO WEB⚠':
        await message.answer('Решил стать Вебмастером проекта TRIGGER? Отлично!\n'
                             'Тогда переходи по ссылке в информационный канал, в \n'
                             'котором ты ознакомишься с основными аспектами \n'
                             'твоей будущей деятельности.✅\n'
                             'Желаем удачи! С уважением TRIGGER_TEAMS❗️\n'
                             'https://t.me/joinchat/sCVGkTC9ojs4YTMy',
                             reply_markup=ReplyKeyboardRemove())

    elif message.text == 'Купить FORECAST ✅':
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

    elif message.text == 'Стать Web master🔥':
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


@dp.message_handler(Text(equals=['Купить 600р✅']))
async def buy_product(message: Message):
    if message.text == 'Купить 600р✅':
        comment = message.from_user.username + "2e"+str(message.from_user.id)
        await message.answer(f'Ты выбрал к покупке продукт FORECAST.\n\n'
                             f'Чтобы оплатить продукт, тебе необходимо \n'
                             f'воспользоваться переводом средств на карту:\n'
                             f'4276 5209 6316 4385 ✅\n\n'
                             f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                             f'Необходимо прикрепить комментарий к платежу:\n'
                             f'{comment}\nИ указать соотвествующую сумму выбранного вами \nпакета❗️\n'
                             f'ℹ️В ином случае твоя покупка будет считаться\n'
                             f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=['Использовать купон - 500р💣']), state=None)
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
                                 f'Твой уровень в TRIGGER - {web.render_lvl}\n'
                                 f'Твоя выплата - {web.user_pay}', reply_markup=ReplyKeyboardRemove())
            break
    else:
        await message.answer('К сожалению ты не являешься партнером TRIGGER\n'
                             'Ознакомься как стать Web master из пункта /menu')


@dp.message_handler(Text(equals=['VIP канал - 250р🔓']))
async def show_vip_channel(message: Message):
    comment = message.from_user.username + '2e' + str(message.from_user.id)
    await message.answer(f'Ты выбрал к покупке VIP чат\n\n'
                         f'Чтобы оплатить продукт, тебе необходимо \n'
                         f'воспользоваться переводом средств на карту:\n'
                         f'4276 5209 6316 4385 ✅\n\n'
                         f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                         f'Необходимо прикрепить комментарий к платежу:\n'
                         f'{comment}\n'
                         f'ℹ️В ином случае твоя покупка будет считаться\n'
                         f'незафиксированной ℹ️',
                         reply_markup=ReplyKeyboardRemove())