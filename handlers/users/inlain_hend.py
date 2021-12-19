# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy
from loader import dp
from states.states import Test
from keyboards.inline.product import pissa, burger, shava, pies


@dp.callback_query_handler(text_contains="pissa")
async def pissal(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Выберите вид Пиццы', reply_markup=pissa)

@dp.callback_query_handler(text_contains="shava")
async def shava1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Выберите вид Шаурмы', reply_markup=shava)


@dp.callback_query_handler(text_contains="burger")
async def burger1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Выберите вид Бургера', reply_markup=burger)


@dp.callback_query_handler(text_contains="pies")
async def pies1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Выберите вид Пирожка', reply_markup=pies)


