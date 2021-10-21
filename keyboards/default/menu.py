from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# from handlers.users.courses import name_course_buy

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить FORECAST ✅'),
            KeyboardButton(text='Курсы 🎓')
        ],

        [
            KeyboardButton('Стать Web master🔥'),
            KeyboardButton('INFO WEB⚠')
        ],
    ],
    resize_keyboard=True
)

show_courses = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton('Информация о курсах')
        ],

        [
            KeyboardButton('Купить курсы')
        ]
    ]
)

choice_courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Py start'),
            KeyboardButton('Py pro'),
            KeyboardButton('Js basics')
        ],
        [
            KeyboardButton('Выбрать пакет')
        ]
    ]
)

select_package = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Py start + Py pro')
        ],
        [
            KeyboardButton('Py pro + Js basics'),
            KeyboardButton('Py start + Js basics')
        ]
    ]
)

buy_course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(f'Использовать купон')
        ],
        [
            KeyboardButton(f'Купить ')
        ]
    ]
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