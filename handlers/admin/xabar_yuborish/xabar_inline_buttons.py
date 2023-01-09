
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
# from inline_btn_maker import  btnRuner

# states
from states.states import AdminState


# reply back
@dp.message_handler(text="🔙 Back", state=AdminState.xabar_inline_buttons)
async def back_from_xabar_yuborish(message:types.Message, state:FSMContext):
    
    await message.answer(
        "orqaqga qaytdik",
        reply_markup=skip_back
    )
    
    await AdminState.previous()



async def btnRuner(text, message: types.Message):

    if text == 'skip⏭':
        return None
    if text == None:
        return None

    
    inline_btns = []
    one_btn = text.split('\n')

    
    btn_list_text = []
    for i in one_btn:
        if i != '':
            btn_list_text.append(i)

    try:  
        for i in btn_list_text:
            btn_value_split = i.split('-')

            
            one_btn_values = []
            for i in btn_value_split:
                if i != '':
                    one_btn_values.append(i)

            inline_btns.append([InlineKeyboardButton(one_btn_values[0], url=one_btn_values[1])])

        return inline_btns
    except:
        await message.answer('Xato tipdagi buttonlarni kiritingiz')

# start xabar yuborish state
@dp.message_handler(content_types=['text'], state=AdminState.xabar_inline_buttons)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    text = message.text
    user_full_name = message.from_user.full_name
    inline_btns = await btnRuner(text, message)

    # state control 
    await state.update_data(
        {
            'inline-btns':inline_btns
        }
    )
    
    
    # send testing for admin
    chat_data = await state.get_data()
    print(
        chat_data
    )
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
        f'Xabar tayyor \n\nFoydalanuvchilarga jo\'nataymi',
        reply_markup=ha_yoq
        )
    
    await AdminState.next()

