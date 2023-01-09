
# bot
from aiogram import types
from loader import dp
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

from .admilar_listView import adminlarListView, adminAddView


@dp.message_handler(text="admin qo'shish", state=AdminState.admin_control)
async def adminAddSet(message: types.Message):

    await message.answer(
            'yangi admin id raqamini va nomini kiriting',
            reply_markup=back_btn
        )

    await AdminState.next()
    

@dp.message_handler(text='🔙 Back', state=AdminState.admin_add)
async def back_from_addAdmin(message: types.Message, state:FSMContext):

    adminlar_royxati_text = await adminlarListView()
    await message.answer(
        """marxamat adminlar ro'yxati\n""" + adminlar_royxati_text,
        reply_markup=adminlar_control
        )
    
    await AdminState.previous()
    
@dp.message_handler(content_types='text', state=AdminState.admin_add)
async def adminlar_controler(message: types.Message):
    
    status_admin_add = await adminAddView(message, AdminState)    

    # if status_admin_add:
