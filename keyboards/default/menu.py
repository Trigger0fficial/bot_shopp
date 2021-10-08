from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить FORECAST ✅'),

        ],
        [
            KeyboardButton('Стать Web master🔥'),
            KeyboardButton('INFO WEB⚠')
        ],
        [

        ]
    ],
    resize_keyboard=True
)

choice = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить 1200р✅'),
            KeyboardButton(text='VIP канал - 250р🔓')
        ],
        [
            KeyboardButton(text='Использовать купон - 1000р💣'),
            KeyboardButton(text='Демо FORECAST🔥')
        ],

    ],
    resize_keyboard=True
)

info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Соглашение'),
            KeyboardButton(text='Тех поддержка')
        ]
    ]
)