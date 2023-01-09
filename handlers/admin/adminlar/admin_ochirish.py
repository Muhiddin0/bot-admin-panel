
# bot
from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext

# env
from env import ADMINS

# keyboards
from keyboards.default.reply_markup_btns import (
        admin_panel_menu,
        adminlar_control,
        back_btn
    )

# states
from states.states import AdminState

from .admilar_listView import adminlarListView, adminAddView, adminDeleteView


@dp.message_handler(text="admini o'chirish", state=AdminState.admin_control)
async def adminAddSet(message: types.Message):

    await message.answer(
            "O'chirish kerak bo'lgan admin id raqamini kiriting",
            reply_markup=back_btn
        )

    await AdminState.admin_delete.set()
    

@dp.message_handler(text='🔙 Back', state=AdminState.admin_delete)
async def back_from_addAdmin(message: types.Message, state:FSMContext):

    adminlar_royxati_text = await adminlarListView()
    await message.answer(
        """marxamat adminlar ro'yxati\n""" + adminlar_royxati_text,
        reply_markup=adminlar_control
        )
    
    await AdminState.admin_control.set()

@dp.message_handler(content_types='text', state=AdminState.admin_delete)
async def adminlar_controler(message: types.Message):

    await adminDeleteView(message, AdminState, dp)    
    await AdminState.admin_control.set()