import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp, db
from aiogram import types


from loader import dp
from states.states import Test


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    flag = await db.select_user(telegram_id=message.from_user.id)
    if flag is not None:
        await message.answer(f'Привет, {message.from_user.full_name}!\n'
                             f'Вы уже зарегестрированы, теперь вы можете ознакомться с нашим меню', reply_markup=menu)
    else:
        await message.answer('Привет!\n'
                             'Это проект Online Столовая здесь вы можете быстро и удобно купить еду\n'
                             'Для начала нужно авторизироваться\n'
                             'Введите ваше имя и фамилию'
                             )
        try:
            user = await db.add_user(telegram_id=message.from_user.id,
                                     full_name=None,
                                     username=None)
        except asyncpg.exceptions.UniqueViolationError:
            user = await db.select_user(telegram_id=message.from_user.id)
        await Test.enter_name.set()



    # a = await db.select_user(telegram_id=message.from_user.id)
    # await db.autoriz_data('dfgdfg', '41424')

    # count = await db.count_users()
    # await Test.enter_name.set()
    # print(count)
    # # Забираем как список или как словарь
    # user_data = list(user)
    # user_data_dict = dict(user)
    #
    # # Забираем напрямую как из списка или словаря
    # username = user.get("username")
    # full_name = user[2]
    #
    # await message.answer(
    #     "\n".join(
    #         [
    #             f'Привет, {message.from_user.full_name}!',
    #             f'Ты был занесен в базу',
    #             f'В базе <b>{count}</b> пользователей',
    #             "",
    #             f"<code>User: {username} - {full_name}",
    #             f"{user_data=}",
    #             f"{user_data_dict=}</code>"
    #         ]))
