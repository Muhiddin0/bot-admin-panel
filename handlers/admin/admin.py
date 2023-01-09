
# bot
from aiogram import types
from loader import dp

# env
from env import ADMINS

# keyboards
from keyboards.default.reply_markup_btns import admin_panel_menu

# states
from states.states import AdminState

# Echo bot
@dp.message_handler(commands=['admin'])
async def chek_admin(message: types.Message):

    user_id = message.from_user.id
    for admin_id in ADMINS:
        if user_id == admin_id[0]:
            await message.answer(
                'salom admin aka botga xush kelibsiz',
                reply_markup=admin_panel_menu
                )
            await AdminState.admin_panel.set()
    