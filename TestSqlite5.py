import sqlite3
import pandas as pd
with sqlite3.connect('db.sqlite3') as conn:
    c = conn.cursor()
    c.execute('select * from account')
    print(pd.DataFrame(c.fetchall()))
    print('ID\tPW')
    print('Test\t1234')