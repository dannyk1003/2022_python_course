import pandas as pd #pip3 install pandas
from sqlalchemy import create_engine #pip3 install sqlalchemy
connstr = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/steam'
engine = create_engine(connstr)

# cur = engine.execute('select * from steam') # use engine.execute to use mysql language
# print(pd.DataFrame(cur))

most_important_x = engine.execute('select developer, genres, categories, positive_ratings/(positive_ratings+negative_ratings) as positive_rate from steam')
print(type(most_important_x))
print(most_important_x)
print(pd.DataFrame(most_important_x))
predict_y = engine.execute('select average_playtime from steam')
print(pd.DataFrame(predict_y))

