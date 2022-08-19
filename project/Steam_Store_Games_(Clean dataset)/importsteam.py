import pandas as pd #pip3 install pandas
from sqlalchemy import create_engine #pip3 install sqlalchemy
connstr = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/steam'
engine = create_engine(connstr)


df_steam = pd.read_csv('steam.csv', sep=',')
#df_steam_description_data = pd.read_csv('steam_description_data.csv', sep=',')
#df_steam_media_data = pd.read_csv('steam_media_data.csv', sep=',')
#df_steam_requirements_data = pd.read_csv('steam_requirements_data.csv', sep=',')
#df_steam_support_info = pd.read_csv('steam_support_info.csv', sep=',')
#df_steamspy_tag_data = pd.read_csv('steamspy_tag_data.csv', sep=',')
print(df_steam.shape[0])
#print(df_steamspy_tag_data.head(10))

#df_steam.to_sql('steam', engine, index=False)
#df_steam_description_data.to_sql('steam_description_data', engine, index=False)
#df_steam_media_data.to_sql('steam_media_data', engine, index=False)
#df_steam_requirements_data.to_sql('steam_requirements_data', engine, index=False)
#df_steam_support_info.to_sql('steam_support_info', engine, index=False)
#df_steamspy_tag_data.to_sql('steamspy_tag_data', engine, index=False)

#print(df_steam.head(5))
#df_steam.head(10).to_sql('steam_t' , engine , index=True)
#df_steam.head(10).to_sql('steam_f' , engine , index=False)
#df = pd.read_sql('titanic',engine)
#print(df)

#pip install pandas
#pip install sqlalchemy
#pip install mysql-connector-python