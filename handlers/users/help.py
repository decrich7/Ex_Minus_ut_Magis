# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from loader import dp


@dp.message_handler(text='/help')
async def bot_start(message: types.Message):
    await message.answer('Для того чтобы начать использовать Бота\n'
                         'Вам следует зарегестрироваться, введя Имя Фамилию и Группу в которой вы обучаетесь\n'
                         'Далее просто следуйте инструкциям, в конце перейдите по ссылке и оплатите товар\n'
                         'Вам будет вадан код, после получения товара она анулируется')