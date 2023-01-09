
# bot
from aiogram import types
from loader import dp

# state fSM
from aiogram.dispatcher import FSMContext

# keyboards
from keyboards.default.reply_markup_btns import (
    admin_panel_menu,
    xabr_types,
    back_item,
    back_btn
    )

# states
from states.states import AdminState


# start xabar yuborish state
@dp.message_handler(text=['Video', 'Audio', 'Photo', 'Text'], state=AdminState.xabar_yuborish)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    text = message.text
    user_full_name = message.from_user.full_name

    # state control
    await state.update_data(
        {
            'message-type':text
        }
    )

    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga {text}ni jo\'nating',
        reply_markup=back_btn
        )
    
    await AdminState.next()
    
@dp.message_handler(text='🔙 Back', state=AdminState.xabar_type)
async def back_from_xabar_yuborish(message:types.Message, state:FSMContext):
    
    await message.answer(
        "orqaqga qaytdik",
        reply_markup=xabr_types
    )
    
    await AdminState.previous()