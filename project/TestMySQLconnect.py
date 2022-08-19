import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/mydb')



df = pd.read_sql_query('select * from air', engine)
print(df.head(5))