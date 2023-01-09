
# bot
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext

# env
from env import ADMINS

# keyboards
from keyboards.default.reply_markup_btns import admin_panel_menu, adminlar_control

# states
from states.states import AdminState

# adminlar list view
# from admilar_listView import adminlarListView
from .admilar_listView import adminlarListView

@dp.message_handler(text='adminlar', state=AdminState.admin_panel)
async def adminlar_controler(message: types.Message):
    
    adminlar_royxati_text = await adminlarListView()
    
    await message.answer(
        """marxamat adminlar ro'yxati\n""" + adminlar_royxati_text,
        reply_markup=adminlar_control
        )

    await AdminState.admin_control.set()
    

@dp.message_handler(text='🔙 Back', state=AdminState.admin_control)
async def back_from_controler(message: types.Message, state:FSMContext):

    await message.answer(
            "asosiy menu",
            reply_markup=admin_panel_menu
        )
    
    await AdminState.first()
    
