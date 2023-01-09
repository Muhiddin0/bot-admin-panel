
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
    back_btn,
    skip_back
    )

# states
from states.states import AdminState

@dp.message_handler(content_types=['video'], state=AdminState.xabar_type)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    video_id = message.video.file_id
    video_captions = message.caption
    user_full_name = message.from_user.full_name

    # state control
    await state.update_data(
        {
            'video':video_id,
            'captions':video_captions
        }
    )

    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga videoni Inline knopkalarni  j\'nating',
        reply_markup=skip_back
        )
    
    await AdminState.next()

@dp.message_handler(content_types=['audio'], state=AdminState.xabar_type)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    audio_id = message.audio.file_id
    audio_captions = message.caption
    user_full_name = message.from_user.full_name

    # state control
    await state.update_data(
        {
            'audio':audio_id,
            'captions':audio_captions
        }
    )

    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga audioni Inline knopkalarni  jo\'nating',
        reply_markup=skip_back
        )
    
    await AdminState.next()

@dp.message_handler(content_types=['photo'], state=AdminState.xabar_type)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    photo_id = message.photo[-1].file_id
    photo_captions = message.caption
    user_full_name = message.from_user.full_name

    # state control
    await state.update_data(
        {
            'photo':photo_id,
            'captions':photo_captions
        }
    )

    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga Rasimni Inline knopkalarni  jo\'nating',
        reply_markup=skip_back
        )
    
    await AdminState.next()

@dp.message_handler(content_types=['text'], state=AdminState.xabar_type)
async def xabar_yuborish_stateRun(message: types.Message, state:FSMContext):

    text = message.text
    user_full_name = message.from_user.full_name

    # state control
    await state.update_data(
        {
            'text':text
        }
    )

    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga Inline knopkalarni jo\'nating',
        reply_markup=skip_back
        )
    
    await AdminState.next()


# reply back
@dp.message_handler(text="🔙 Back", state=AdminState.xabar_inline_buttons)
async def back_from_xabar_yuborish(message:types.Message, state:FSMContext):
    
    user_full_name = message.from_user.full_name
    
    await message.answer(
        f'Yaxshi {user_full_name} aka\n\nEndi Menga Textni jo\'nating',
        reply_markup=back_btn
    )
    
    await AdminState.previous()
    
 
