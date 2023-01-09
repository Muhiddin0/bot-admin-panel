
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

import sqlite3

db = sqlite3.connect('data/users.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (user_id INT) """)
db.commit()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    user_id = message.from_user.id

    sql.execute(f"""SELECT * FROM users WHERE user_id = {user_id}""")
    user_auth_cheker = bool(sql.fetchall())

    if not user_auth_cheker:
        sql.execute(f"""INSERT INTO users VALUES ({user_id})""")
        db.commit()
    
    await message.answer(
        f"Assalomu alaykum, <a href='tg://user?id={user_id}'>{message.from_user.full_name}!</a>",
        reply_markup=ReplyKeyboardRemove()
        )
