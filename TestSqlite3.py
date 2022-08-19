import sqlite3
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()
# c.execute('''
# create table account(
#     ID text,
#     PW text
# )
# ''')
# conn.commit()
# conn.close()


with sqlite3.connect('db.sqlite3') as conn:
    c = conn.cursor()
    c.execute('''
    create table account(
        ID text,
        PW text
    )
    ''')
