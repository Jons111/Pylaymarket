from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bolalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1',callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3',callback_data='3'),
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5')
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='⬅️'),
            InlineKeyboardButton(text='➡️', callback_data='➡️')

        ]
    ]
)