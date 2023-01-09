

async def btnRuner(text):

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

        
    for i in btn_list_text:
        btn_value_split = i.split('-')

        
        one_btn_values = []
        for i in btn_value_split:
            if i != '':
                one_btn_values.append(i)

        inline_btns.append([InlineKeyboardButton(one_btn_values[0], url=one_btn_values[1])])

    return inline_btns
