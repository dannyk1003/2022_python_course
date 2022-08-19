import mysql.connector
with mysql.connector.connect(user = 'root', password = 'Tcfst123456!', host = '127.0.0.1', database = 'myDB') as conn:
    c = conn.cursor()
    c.execute('select * from air')
    data = c.fetchall()
    print(data)


# import mysql.connector
# with mysql.connector.connect(user='root', password='Tcfst123456!',host='127.0.0.1', database='mydb') as conn:
#     c = conn.cursor()
#     c.execute('SELECT * FROM air')
#     data = c.fetchall()
#     print(data)

# import pandas as pd

# print(pd.DataFrame(data))