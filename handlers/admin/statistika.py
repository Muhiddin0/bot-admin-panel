
# bot
from aiogram import types
from loader import dp

# states
from states.states import AdminState

import sqlite3


# data base
db = sqlite3.connect("data/users.db")
sql = db.cursor()

@dp.message_handler(text="statistika", state=AdminState.admin_panel)
async def adminAddSet(message: types.Message):

    sql.execute("""SELECT * FROM users""")
    
    await message.answer(
            f"botda <b>{len(sql.fetchall())} ta</b> foydalanuvchi bor",
        )