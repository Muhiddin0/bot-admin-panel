
# bot
from aiogram import types
from loader import dp

# env
from env import ADMINS

# keyboards
from keyboards.default.reply_markup_btns import admin_panel_menu

# states
from states.states import AdminState

admin_states = (
    AdminState.admin_panel,
    AdminState.xabar_yuborish,
    AdminState.xabar_type,
    AdminState.xabar_inline_buttons,
    AdminState.xabar_yuborish_cheked,
    AdminState.admin_control,
    AdminState.admin_add,
    AdminState.admin_delete
)

for i in range(int(len(admin_states))):
        
    @dp.message_handler(commands=['start'], state=admin_states[i])
    async def chek_admin(message: types.Message):

        user_id = message.from_user.id
        for admin_id in ADMINS:
            if user_id == admin_id:
                await message.answer(
                    'bot siz uchun qayta faolashtirildi',
                    reply_markup=admin_panel_menu
                    )
                await AdminState.admin_panel.set()
        