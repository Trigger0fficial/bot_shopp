from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Py start ❗'),
            KeyboardButton('Py pro ❗'),
                KeyboardButton('C_UNITY ❗')
        ],
        [
            KeyboardButton('❗Py start + Py pro❗'),
            KeyboardButton('❗Py pro + C_UNITY❗'),
            KeyboardButton('❗Py start + C_UNITY❗')
        ]
    ]
)

