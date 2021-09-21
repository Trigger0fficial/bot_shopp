from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default import menu
from keyboards.default.menu import choice
from loader import dp


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


dp.message_handler(Text(equals='Купить 600р'))


async def buy_product(message: Message):
    if message.text == 'Купить 600р':
        await message.answer('Вы купили продукт!', reply_markup=ReplyKeyboardRemove())
