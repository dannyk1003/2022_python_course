import sqlite3
with sqlite3.connect('db2.sqlite3') as conn:
    c = conn.cursor()
    c.execute('''
    create table account(ID text, PW text)
    ''')


# with sqlite3.connect('db2.sqlite3') as conn:
#     c = conn.cursor()
#     c.execute('''
#     create table account(
#         ID text,
#         PW text
#     )
#     ''')
