# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback, buy

choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Пиццы", callback_data=buy_callback.new(item_name="pissa")),
        InlineKeyboardButton(text="Бургеры", callback_data=buy_callback.new(item_name="burger"))
    ],
    [
        InlineKeyboardButton(text="Шаурма", callback_data=buy_callback.new(item_name="shava")),
        InlineKeyboardButton(text="Пирожки", callback_data=buy_callback.new(item_name="pies")),
    ]
])

shava = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Шаурма с сосиской - 70 руб.",
                             callback_data=buy.new(item_name="shava_buy", prise='70', type='Шаурма с сосиской')),
    ],
    [
        InlineKeyboardButton(text="Шаурма с люля - 85 руб.", callback_data=buy.new(item_name="shava_buy", prise='85', type='Шаурма с люля')),
    ],
    [
        InlineKeyboardButton(text="Шаурма курицей - 110 руб.",
                             callback_data=buy.new(item_name="shava_buy", prise='110', type='Шаурма курицей')),
    ]
])

pissa = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кусок пиццы - 50 руб.",
                             callback_data=buy.new(item_name="pissa_buy", prise='50', type='Кусок пиццы')),
    ],
    [
        InlineKeyboardButton(text="Большая пицца - 85 руб.",
                             callback_data=buy.new(item_name="pissa_buy", prise='85', type='Большая пицца')),
    ]
])

burger = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Бургер с курицей - 65 руб.",
                             callback_data=buy.new(item_name="burger_buy", prise='65', type='Бургер с курицей'))
    ],
    [
        InlineKeyboardButton(text="Бургер с говядиной - 110 руб.",
                             callback_data=buy.new(item_name="burger_buy", prise='110', type='Бургер с говядиной'))
    ]
])

pies = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Пирожок с капустой - 30 руб.",
                             callback_data=buy.new(item_name="pies_buy", prise='5', type='Пирожок с капустой'))
    ],
    [
        InlineKeyboardButton(text="Пирожок с мясом - 45 руб.",
                             callback_data=buy.new(item_name="pies_buy", prise='45', type='Пирожок с мясом'))
    ],
    [
        InlineKeyboardButton(text="Пирожок с картофелем - 35 руб.",
                             callback_data=buy.new(item_name="pies_buy", prise='35', type='Пирожок с картофелем'))
    ]
])
