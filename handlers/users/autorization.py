# -*- coding: utf-8 -*-


from aiogram.dispatcher import FSMContext
from keyboards.default import menu

from loader import dp, db
from aiogram import types


from loader import dp
from states.states import Test


@dp.message_handler(state=Test.enter_name)
async def name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer('Введите свою группу!')
    await Test.next()


@dp.message_handler(state=Test.group)
async def name(message: types.Message, state: FSMContext):
    group = message.text
    data = await state.get_data()
    name = data.get("name")
    await db.autoriz_data(name, group, message.from_user.id)
    await message.answer("Вы успешно зарегестрировались!\n"
                         "Теперь вы можете ознакомится с нашим меню", reply_markup=menu)
    await state.finish()

