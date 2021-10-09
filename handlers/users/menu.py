from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep

from handlers.users.status_web import user_date, user_all_count, user_lvl, user_pay
from keyboards.default import menu
from keyboards.default.menu import choice, info
from loader import dp
from states.verification_coupon import State_coupon

price_forecast = 1000
price_web_master = 1200
all_web = [1935538508, ]
lvl_web = {'aff': 0.2, 'new_web': 0.35, 'web': 0.3}
list_admin = [745832259, 869546657]


class Web_master:
    def __init__(self, user_id, user_name, user_date, user_all_count_invited=0, user_lvl='x1', render_lvl='web',
                 aff=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date = user_date
        self.user_all_count_invited = user_all_count_invited
        self.user_count_invited = 0
        self.render_lvl = render_lvl
        self.user_pay = 0
        self.lvl = user_lvl
        self.aff = aff

    def profit_web(self, lvl):
        self.user_count_invited += 1
        self.user_all_count_invited += 1
        if self.aff == None:
            self.user_pay += 0.4 * price_forecast
        else:
            self.user_pay += lvl * price_forecast

    def paid_web(self):
        self.user_pay = 0
        self.user_count_invited = 0

    def __str__(self):
        return f'-----------------------Web_master---------------------------\n' \
               f'Name_web: {self.user_name}\nId_web: {self.user_id}\n' \
               f'Date_web: {self.user_date}\nLvl_web: {self.render_lvl}\n' \
               f'Total_user: {self.user_all_count_invited}  Now_user: {self.user_count_invited}\n' \
               f'Pay_web: {self.user_pay}\n' \
               f'Invited - {self.aff}'


class Affiliates(Web_master):

    def __init__(self, user_id, user_name, user_date):
        super().__init__(user_id=user_id, user_name=user_name, user_date=user_date, user_lvl='x1', render_lvl='web')
        self.web_count = 0
        self.total_web_invited = 0
        self.web_invited = 0
        self.pay_new_web = 0
        self.pay_act_web = 0
        self.total_pay = 0

    def profit_web(self, lvl):
        for web_master in list_web_master:
            if web_master.aff == self.user_id:
                self.total_web_invited += web_master.user_all_count_invited
                self.pay_act_web += web_master.user_all_count_invited * price_web_master * lvl

    def new_web_master(self, lvl):
        for web_master in list_web_master:
            if web_master.aff == self.user_id:
                self.web_count += 1
                self.pay_new_web += lvl * price_web_master



    def __str__(self):
        return f'-----------------------Affiliates---------------------------\n' \
               f'Name_web: {self.user_name}\nId_web: {self.user_id}\n' \
               f'Date_web: {self.user_date}\nLvl_web: {self.render_lvl}\n' \
               f'Total_user: {self.web_count}  Act_web: {self.total_web_invited}\n' \
               f'Pay_new_web: {self.pay_new_web}\n' \
               f'Pay_act_web: {self.pay_act_web}' \



list_affiliates = [
    Affiliates(user_id=1234, user_name='Test', user_date='08.10'),
    Affiliates(user_id=4321, user_name='Sasha', user_date='09.10')
]

list_web_master = [
    Web_master(user_id=1935538508, user_name='Misha', user_date='25.09', render_lvl='web', aff=4321),
    Web_master(user_id=1935538504, user_name='Dima', user_date='25.09', render_lvl='web', aff=4321),
    Web_master(user_id=1935538504, user_name='Dima', user_date='25.09', render_lvl='web', aff=4321),
    Web_master(user_id=1935538504, user_name='Test', user_date='25.09', render_lvl='web', aff=4321)

]


def activity_affiliates():
    for all_aff in list_affiliates:
        all_aff.profit_web(lvl=lvl_web['aff'])
        all_aff.new_web_master(lvl=lvl_web['new_web'])

    for aff in list_affiliates:
        print(aff.__str__())


def activity_web_master():
    list_web_master[0].profit_web(lvl=lvl_web['web'])
    list_web_master[0].profit_web(lvl=lvl_web['web'])
    list_web_master[0].profit_web(lvl=lvl_web['web'])
    list_web_master[0].profit_web(lvl=lvl_web['web'])
    list_web_master[-1].profit_web(lvl=lvl_web['web'])
    list_web_master[-1].profit_web(lvl=lvl_web['web'])
    list_web_master[-1].profit_web(lvl=lvl_web['web'])
    list_web_master[-1].profit_web(lvl=lvl_web['web'])

    for web in list_web_master:
        print(web.__str__())


def admin_trigger():
    web_total_pay = 0
    web_total = 0
    web_total_count_invited = 0
    aff_total_pay = 0
    aff_total = 0
    aff_total_count_invited = 0
    for web in list_web_master:
        web_total_pay += web.user_pay
        web_total_count_invited += web.user_all_count_invited
        web_total += 1

    for affiliates in list_affiliates:
        aff_total_pay += affiliates.user_pay
        aff_total_count_invited += affiliates.user_all_count_invited
        aff_total += 1

    print(f'\n--------Admin---------\n'
          f'\n-------Web-------\n'
          f'Total web: {web_total}\n'
          f'All invited: {web_total_count_invited}\n'
          f'Pay total: {web_total_pay}\n'
          f'\n-------Affiliates-------\n'
          f'Total affiliates: {aff_total}\n'
          f'All invited: {aff_total_count_invited}\n'
          f'Pay total: {aff_total_pay}\n')

    activity_web_master()
    activity_affiliates()


admin_trigger()


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Что ты хочешь сделать?',
                         reply_markup=menu)


@dp.message_handler(Text(equals=['Купить FORECAST ✅', 'Стать Web master🔥',
                                 'INFO WEB⚠', ]))
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
                             'Стоимость нашего продукта - 1200₽. Но его можно приобрести\n'
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


@dp.message_handler(Text(equals=['Купить 1200р✅']))
async def buy_product(message: Message):
    if message.text == 'Купить 1200р✅':
        comment = message.from_user.username + "2e" + str(message.from_user.id)
        await message.answer(f'Ты выбрал к покупке продукт FORECAST.\n\n'
                             f'Чтобы оплатить продукт, тебе необходимо \n'
                             f'воспользоваться переводом средств на карту:\n'
                             f'4276 5209 6316 4385 ✅\n\n'
                             f'❗️Важно❗️Чтобы платёж прошёл успешно:\n'
                             f'Необходимо прикрепить комментарий к платежу:\n'
                             f'{comment}\nИ указать соотвествующую сумму выбранного вами \nпакета❗️\n'
                             f'ℹ️В ином случае твоя покупка будет считаться\n'
                             f'незафиксированной ℹ️', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=['Использовать купон - 1000р💣']), state=None)
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


@dp.message_handler(Command('admin'))
async def show_admin(message: Message):
    if message.from_user.id in list_admin:
        for web in list_web_master:
            await message.answer(web.__str__())
    else:
        await message.answer('Информация недоступна!\n'
                             'Ты не являешься администратором проекта')


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


@dp.message_handler(Text(equals=['Демо FORECAST🔥']))
async def show_demo(message: Message):
    await message.answer('В разработке.', reply_markup=ReplyKeyboardRemove())
