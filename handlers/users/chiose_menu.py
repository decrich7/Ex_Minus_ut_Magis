# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext

from data import config
from aiogram.utils.markdown import hlink, hcode

from keyboards.inline.pay import paid_keyboard
from loader import dp, db
from aiogram import types
from aiogram.types import Message, CallbackQuery
from keyboards.inline.product import choice
from loader import dp
from states.states import Test
from keyboards.inline.callback_datas import buy
from utils.misc.qiwi import Payment


@dp.message_handler(text='Меню 📝')
async def bot_start(message: types.Message):
    await message.answer('Выберите категорию 📋', reply_markup=choice)




@dp.callback_query_handler(buy.filter(item_name="pies_buy"))
async def buying(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    prise = callback_data.get("prise")
    type = callback_data.get("type")
    payment = Payment(amount=prise)
    payment.create()
    await call.message.answer(
        "\n".join([
            f"Оплатите не менее {prise} ₽ по номеру телефона или по адресу",
            hlink(config.WALLET_QIWI, url=payment.invoice),
            "Или обязательно укажите ID платежа:",
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard)
    await state.set_state("qiwi")
    await state.update_data(payment=payment, tovar='Пирожок', prise=prise, type=type)

@dp.callback_query_handler(buy.filter(item_name="burger_buy"))
async def buying1(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    prise = callback_data.get("prise")
    type = callback_data.get("type")
    payment = Payment(amount=prise)
    payment.create()
    await call.message.answer(
        "\n".join([
            f"Оплатите не менее {prise} ₽ по номеру телефона или по адресу",
            hlink(config.WALLET_QIWI, url=payment.invoice),
            "И обязательно укажите ID платежа:",
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard)
    await state.set_state("qiwi")
    await state.update_data(payment=payment, tovar='Бургер', prise=prise, type=type)


@dp.callback_query_handler(buy.filter(item_name="pissa_buy"))
async def buying2(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    prise = callback_data.get("prise")
    type = callback_data.get("type")
    payment = Payment(amount=prise)
    payment.create()
    await call.message.answer(
        "\n".join([
            f"Оплатите не менее {prise} ₽ по номеру телефона или по адресу",
            hlink(config.WALLET_QIWI, url=payment.invoice),
            "И обязательно укажите ID платежа:",
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard)
    await state.set_state("qiwi")
    await state.update_data(payment=payment, tovar='Пицца', prise=prise, type=type)


@dp.callback_query_handler(buy.filter(item_name="shava_buy"))
async def buying2(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    prise = callback_data.get("prise")
    prise = callback_data.get("prise")
    type = callback_data.get("type")
    payment = Payment(amount=prise)
    payment.create()
    await call.message.answer(
        "\n".join([
            f"Оплатите не менее {prise} руб. по номеру телефона или по адресу",
            hlink(config.WALLET_QIWI, url=payment.invoice),
            "И обязательно укажите ID платежа:",
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard)
    await state.set_state("qiwi")
    await state.update_data(payment=payment, tovar='Шаурма', prise=prise, type=type)
