
# bot
from aiogram import types
from loader import dp

# state fSM
from aiogram.dispatcher import FSMContext

# keyboards
from keyboards.default.reply_markup_btns import admin_panel_menu, xabr_types, back_item

# states
from states.states import AdminState


# start xabar yuborish state
@dp.message_handler(text='xabar yuborish', state=AdminState.admin_panel)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    await message.answer(
        'qanday xabar yuboramiz\n\n<b>Video\nAudio\nPhoto\nText</b>',
        reply_markup=xabr_types
        )
    
    await AdminState.next()
    
@dp.message_handler(text='🔙 Back', state=AdminState.xabar_yuborish)
async def back_from_xabar_yuborish(message:types.Message, state:FSMContext):
    
    await message.answer(
        "asosiy bo'limga qaytdik",
        reply_markup=admin_panel_menu
    )
    
    await AdminState.previous()