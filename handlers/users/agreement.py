from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(Command('agreement'))
async def show_agreement(message: Message):
    await message.answer('❗Пользовательское соглашение❗️\n'
                         'Владельцами данного проекта являются @keepeero\n'
                         '1 - Порядок покупки продуктов следующий:\n'
                         '1.1 - Нажать кнопку "меню"\n'
                         '1.2 - Нажать кнопку "запустить бота /start"\n'
                         '1.3 - Нажать кнопку "/menu"\n'
                         '1.4 - Нажать кнопку "Купить(название продукта)"\n'
                         '1.5 - Нажать кнопку "Купить 600Р"\n'
                         'После чего выполнить онлайн перевод на банковскую \n'
                         'карту и указать коментарий  к переводу который вам\n'
                         'выдаст бот\n'
                         '1.6 - Нажать кнопку "Использовать купон - 500Р"\n'
                         '1.6.1 - Ввести купон после чего повторить все \n'
                         'действия как и в пункте 1.5\n'
                         '1.7 - Нажать кнопку "VIP Канал - 250Р"\n'
                         'После чего выполнить все действия как в пунктах 1.5, 1.6\n\n'
                         '2 - Порядок покупки реферальной программы\n'
                         '2.1 - Прежде чем покупать доступ к реферальной \n'
                         'программе проекта TRIGGER нажмите на кнопку "INFO\n'
                         'WEB" и ознкомьтесь с информацией о реферальной \n'
                         'программе проекта, а так же о деятельности Вебмастера.\n'
                         '2.2 - После ознакомления с выше сказанным каналом, \n'
                         'нажимаем на кнопку "Стать Web master"\n'
                         'После вам нужно написать на аккаунт администрации \n'
                         'проекта TRIGGER  @keepeero и прислать кодовое слово \n'
                         'которое вам выдал бот, администрация ответит вам в \n'
                         'течении 10-15 мин.\n\n'
                         '3 - Ответственность за то, что пользователь использует\n'
                         'данные продукты по отношению к букмекерским \n'
                         'конторам проект TRIGGER не несет!!!\n'
                         '4 - Распространение данных проекта TRIGGER, а так же\n'
                         'данных участников данного проекта строго запрещено\n'
                         'в противном случаи пользователю грозит бан в проекте!!!\n'
                         '5 - Возврат денежных средств в проекте TRIGGER не \n'
                         'предусмотрен!!!\n'
                         '6 - Нарушение правил в чатах проекта карается баном!!!\n'
                         '7 - Любые виды мошенничества по отношению к \n'
                         'проекту TRIGGER, а так же по отношению к участникам\n'
                         'проекта караются баном!!!\n'
                         '8 - Все действия выполняемые Вебмастерами и \n'
                         'пользователями в проекте, отслеживаются \n'
                         'администрацией.\n\n'
                         'С уважением, владельцы проекта TRIGGER @keepeero')