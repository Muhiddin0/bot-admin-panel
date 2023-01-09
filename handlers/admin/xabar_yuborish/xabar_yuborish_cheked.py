
# bot
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

# state fSM
from aiogram.dispatcher import FSMContext

# keyboards
from keyboards.default.reply_markup_btns import (
    admin_panel_menu,
    xabr_types,
    back_item,
    back_btn,
    skip_back,
    ha_yoq
    )
from states.states import AdminState


# start xabar yuborish state
@dp.message_handler(text=['Jo\'nat'], state=AdminState.xabar_yuborish_cheked)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    # all chat data
    chat_data = await state.get_data()
    inline_btns = chat_data['inline-btns']
    
    if chat_data['message-type'] == 'Video':
        
        await message.answer_video(
            video=chat_data['video'],
            caption=chat_data['captions'],
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_btns)
        )
   
    elif chat_data['message-type'] == 'Photo':
        
        await message.answer_photo(
            photo=chat_data['photo'],
            caption=chat_data['captions'],
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_btns)
        )
    
    elif chat_data['message-type'] == 'Audio':
        
        await message.answer_audio(
            audio=chat_data['audio'],
            caption=chat_data['captions'],
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_btns)
        )
    
    elif chat_data['message-type'] == 'Text':
        
        await message.answer(
            text=chat_data['text'],
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_btns)
        )
    
    await message.answer(
        f'xabar yuborildi',
        reply_markup=admin_panel_menu
        )
    
    await AdminState.first()
 

@dp.message_handler(text=['Bekor qil'], state=AdminState.xabar_yuborish_cheked)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):
    await message.answer(
            text='Bekor qilndi',
            reply_markup=admin_panel_menu
        )
    await AdminState.first()