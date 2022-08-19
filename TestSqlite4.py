import sqlite3
with sqlite3.connect('db.sqlite3') as conn:
    c = conn.cursor()
    c.execute('''
    insert into account(ID,PW) values("test", "1234")
    ''')
    #select * from account

print(c)