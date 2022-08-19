import sqlite3
with sqlite3.connect('db2.sqlite3') as conn:
    c = conn.cursor()
    c.execute(f'''
    select * from account
    ''')
    data = c.fetchall() # data = [('test', '1234'), ('danny', '0000')]
    print(data)
    print('ID\tPW')
    for [id, pw] in data:
        print(id, pw, sep='\t')

