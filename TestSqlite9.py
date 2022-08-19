import sqlite3
with sqlite3.connect('db2.sqlite3') as conn:
    c = conn.cursor()
    while True:
        account_ID = input('enter ID: ')
        account_PW = input('enter PW: ')
        c.execute('''
        select * from account where ID = ? and PW = ?
        ''', (account_ID, account_PW))
        data = c.fetchall() # data = [('test', '1234'), ('danny', '0000')]

        if len(data) == 0 :
            print('login failed!  plz try again~')
        elif len(data) > 0:
            print('login success!')
            break
