import logging

from aiogram import Dispatcher

from env import ADMINS

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin[0], "Bot faollashdi!")

        except Exception as err:
            logging.exception(err)
