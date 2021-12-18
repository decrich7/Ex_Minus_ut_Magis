# -*- coding: utf-8 -*-
import random
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode, hlink
from loader import db
from loader import dp
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney

@dp.callback_query_handler(text="cancel", state="qiwi")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Отменено")
    await state.finish()


@dp.callback_query_handler(text="paid", state="qiwi")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена.")

        return
    except NotEnoughMoney:
        await call.message.answer("Оплаченная сума меньше необходимой.")
        return

    else:
        await call.message.answer("Успешно оплачено")
        id_buy = random.randint(10000, 90000)
        await db.add_inf_tovar(data['type'], str(id_buy), call.message.chat.id)
    await call.message.edit_reply_markup()
    await state.finish()
