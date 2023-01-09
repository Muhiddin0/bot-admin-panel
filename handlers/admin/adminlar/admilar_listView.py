
import sqlite3
from aiogram import types
from keyboards.default.reply_markup_btns import adminlar_control, start_btn
from states.states import AdminState

# connect data base
db = sqlite3.connect('data/adminlar.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS adminlar ( id INT, name TEXT)""")



async def text_formater(text):

    text_split = text.split(' ')
    admin_addJson = {
            'admin-id':'',
            'admin-name':''
        }

    for i in text_split:
        if i != '':
            if i.isdigit():
                admin_addJson['admin-id'] = i
            else:
                admin_addJson['admin-name'] += i + ' '

    return admin_addJson


async def adminlarListView():

    sql.execute("""SELECT rowid, * FROM adminlar""")
    sql_data = sql.fetchall()

    adminlar_royxati_text = ''
    for i in sql_data:
        adminlar_royxati_text += f"""\nID <b>{i[0]})</b>\n<a href='tg://user?id={i[1]}'>{i[2]}</a>\n"""
    
    return adminlar_royxati_text

async def adminAddView(message:types.Message, AdminState):

    user_text = message.text

    admin_datas = await text_formater(user_text)

    if not admin_datas['admin-id'].isdigit():
        await message.answer(text='xato admin id raqami')
        return
        

    print(admin_datas)
    
    admin_id = admin_datas['admin-id']
    admin_name = admin_datas['admin-name']
    
    sql.execute(f"""SELECT rowid, * FROM adminlar WHERE id = {admin_id}""")
    cheked_base = bool(sql.fetchall())

    if cheked_base:
        await message.answer('''Ushbu foydalanuvchi shundoq ham bazada mavjud''')

    else:

        sql.execute(f"""INSERT INTO adminlar VALUES ({admin_id}, '{admin_name}') """)
        db.commit()

        adminlar_royxati_text = await adminlarListView()
        await message.answer(
                """marxamat adminlar ro'yxati\n""" + adminlar_royxati_text,
                reply_markup=adminlar_control
            )
            
        await message.answer('''foydalanuvchi adminlar qatoriga qo'shildi ''')
        await AdminState.previous()

async def adminDeleteView(message:types.Message, AdminState, dp):

    text = message.text
    if not text.isdigit():
        await message.answer('''Xato qiymat kiritingiz''')
        return

    try:
        sql.execute(f"""SELECT * FROM adminlar WHERE rowid = {text}""")
        delete_admin_id = sql.fetchall()
        
        sql.execute(f"""DELETE FROM adminlar WHERE rowid = {text}""")
        db.commit()
        sql.execute("""SELECT rowid, * FROM adminlar""")

        await message.answer(
            '''Foydalanuvchi adminlar qatoridan chiqarib yuborildi''',
            )

            
        adminlar_royxati_text = await adminlarListView()
        await message.answer(
            """marxamat adminlar ro'yxati\n""" + adminlar_royxati_text,
            reply_markup=adminlar_control
            )
        try:
            await dp.bot.send_message(
                    chat_id=int(delete_admin_id[0][0]),
                    text="siz adminlar qatoridan chiqarildingiz",
                    reply_markup=start_btn
                )
        except:
            pass


        await AdminState.admin_control.set()
        
    except:
        await message.answer("""Admin id raqami xato bo'lganligi sabab ish bajarilmadi""")

