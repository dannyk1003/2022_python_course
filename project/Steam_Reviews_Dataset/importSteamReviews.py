import pandas as pd #pip3 install pandas
from sqlalchemy import create_engine #pip3 install sqlalchemy
conn_str = 'mysql+mysqlconnector://root:Tcfst123456!@localhost:3306/steam'
engine = create_engine(conn_str)

review_file_list = ['reviews-1-115.csv', 'reviews-115-1230.csv', 'reviews-1230-2345.csv', 'reviews-2345-4575.csv', 'reviews-4575-6805.csv', 'reviews-6805-9035.csv', 'reviews-9035-11265.csv', 'reviews-11265-13495.csv', 'reviews-13495-13500.csv', 'reviews-13500-13537.csv', 'reviews-13537-27075.csv']

df_steam_reviews_dataset_list = []

for i in review_file_list:
    df_reviews = pd.read_csv(i, sep=',')
    del df_reviews['review']
    df_steam_reviews_dataset_list.append(df_reviews)



df_reviews_1_115 = pd.read_csv('reviews-1-115.csv', sep=',')

del df_reviews_1_115['review'] # delete review colum

print(df_reviews_1_115.shape[0])

df_reviews_1_115.to_sql('steam_reviews_data', engine, index=False, if_exists='append')
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