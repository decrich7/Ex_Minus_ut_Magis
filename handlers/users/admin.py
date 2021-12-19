# -*- coding: utf-8 -*-

import asyncpg
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from data import config
from keyboards.default import menu
from loader import dp, db
from aiogram import types

from states.states import Send
from loader import dp
from states.states import Test


@dp.message_handler(text='/admin')
async def bot_start(message: types.Message):

    if str(message.from_user.id) in config.ADMINS:
        await message.answer('Здравствуйте!\n'
                             'Вы находитесь в админ панели\n'
                             '/send_message - Команда для массовой рассылки\n'
                             '/url_admin - Команда для перехода в ВЕБ-интерфейс админ панели')



@dp.message_handler(text='/send_message')
async def bot_start(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in config.ADMINS:
        await message.answer('Введите сообщения для расслыки все пользователем')
        await Send.enter_message.set()

@dp.message_handler(state=Send.enter_message)
async def bot_start(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in config.ADMINS:
        message = message.text
        users = await db.select_all_users()
        for i in users:
            await dp.bot.send_message(i[3], message)
    await state.finish()

@dp.message_handler(text='/url_admin')
async def bot_start(message: types.Message):
    if str(message.from_user.id) in config.ADMINS:
        await message.answer('Ссылка на бота')