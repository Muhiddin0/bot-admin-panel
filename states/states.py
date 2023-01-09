from aiogram.dispatcher.filters.state import State, StatesGroup

class AdminState(StatesGroup):
    
    # start admin panel
    admin_panel = State()

    # xabar yuborish
    xabar_yuborish = State()
    xabar_type = State()
    xabar_inline_buttons = State()
    xabar_yuborish_cheked = State()

    # adminlar cotrol 
    admin_control = State()
    admin_add = State()
    admin_delete = State()
    
    #
    