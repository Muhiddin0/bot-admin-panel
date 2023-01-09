
import sqlite3

BOT_TOKEN = "5905760146:AAEVDPQVSHNChizv6ru62RopUFsnRog2ZAc"

db = sqlite3.connect("data/adminlar.db")
sql = db.cursor()
sql.execute("""SELECT * FROM adminlar""")

ADMINS = sql.fetchall()
print(ADMINS)