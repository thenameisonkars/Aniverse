import pandas as pd
import time
data=pd.read_csv(r"C:\Users\91877\OneDrive\Desktop\python\Anime_Recommendation_system\anime_database.csv")
list_of_ID=data['anime_id']

#Now we have the list of MAL ids of all anime in list_of_ID
#Now we will work on getting info using IDs from the Jikan API

import requests
import json
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="minakshi*",
    database="Database_Anime"      
    )
mycursor=db.cursor()

#Database for anime ID https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database
counter=0
base_url="https://api.jikan.moe/v4/anime/{}"
anime_id=[1,39535]
for x in list_of_ID:
    url=base_url.format(x)
    response=requests.get(url)
    data=response.json()['data']

    english_name=data['title_english']
    japanese_name=data['title_japanese']
    score=data['score']
    genre=data['genres']
    rank=data['rank']
    popularity=data['popularity']
    list_of_genre=[]

    for element in genre:
        placeholder=element['name']
        list_of_genre.append(placeholder)
    
    new_list_of_genre=[item.replace("'", '"') for item in list_of_genre]
    genre_str=", ".join(new_list_of_genre)

    #Entering data into tables
    db.start_transaction()
    insert_table1="""INSERT INTO list_of_ids (id,title)
                    VALUES (%s,%s)"""
    mycursor.execute(insert_table1,(x,english_name))

    insert_table2="""INSERT INTO anime_info (id,title,genre,score)
                    VALUES (%s,%s,%s,%s) """
    mycursor.execute(insert_table2,(x,english_name,genre_str,score))

    insert_table3="""INSERT INTO pop_and_rank (id,title,ranking,popularity)
                    VALUES (%s,%s,%s,%s)"""
    mycursor.execute(insert_table3,(x,english_name,rank,popularity))
    db.commit()
    counter+=1
    print(counter)
    time.sleep(1)

    #Now we have our database ready


