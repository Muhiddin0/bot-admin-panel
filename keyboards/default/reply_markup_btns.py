
from aiogram.types import ReplyKeyboardMarkup

start_btn = ReplyKeyboardMarkup(
    keyboard=[['/start']],
    resize_keyboard=True,
    )

back_item = ['🔙 Back']
back_btn = ReplyKeyboardMarkup([back_item], resize_keyboard=True)

skip_back = ReplyKeyboardMarkup(
        [
            [back_item[0], 'skip⏭']
        ], resize_keyboard=True
    )

ha_yoq = ReplyKeyboardMarkup(
        [
            ['Jo\'nat', 'Bekor qil']
        ], resize_keyboard=True
    )

admin_panel_menu = ReplyKeyboardMarkup(
        keyboard = [
            ['xabar yuborish', 'majburiy obuna'],
            ['adminlar', 'statistika']
        ],
        resize_keyboard=True
    )

xabr_types = ReplyKeyboardMarkup(
        keyboard = [
            ['Video', 'Audio'],
            ['Photo', 'Text'],
            ['🔙 Back']
        ],
        resize_keyboard=True
    )

adminlar_control = ReplyKeyboardMarkup(
    keyboard=[
        ["admin qo'shish", "admini o'chirish"],
        back_item
    ], resize_keyboard=True
)