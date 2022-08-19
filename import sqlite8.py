import sqlite3
with sqlite3.connect('db2.sqlite3') as conn:
    c = conn.cursor()
    account_ID = input('enter ID: ')
    account_PW = input('enter PW: ')
    c.execute(f'''
    insert into account(ID, PW)
    values("{account_ID}", "{account_PW}")
    ''')

