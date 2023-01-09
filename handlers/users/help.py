from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
# from aiogram.methods.res

from loader import dp, bot


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):

        await message.forum_topic_closed()
        await bot.s

