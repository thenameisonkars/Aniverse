#This file will deal with sorting of the data which we collected in our database according to the user
import pandas as pd
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="minakshi*",
    database="Database_Anime"
    )
mycursor=db.cursor()

choice=1

def match_choice(choice):
    if choice == 1:
        find_anime_id()
    elif choice == 2:
        find_anime_genre()
    elif choice == 3:
        find_anime_score()
    elif choice == 4:
        find_anime_rank()
    elif choice == 5:
        find_anime_pop()
    else:
        print("")
        
#To find anime id based on keywords
def find_anime_id():
    print(" ")
    keyword=input("Enter a keyword from the anime title: ")
    name_pattern=f'%{keyword}%'
    query="""SELECT *
             FROM list_of_ids
             WHERE title LIKE %s 
    """
    df=pd.read_sql(query,db,params=(name_pattern,))
    print(df)

#To find anime based on genre(s) defined by the user
def find_anime_genre():
    print(" ")
    list_of_genre=[]
    while True:
        genre=input("Enter genre(leave blank if none): ")
        if genre == "":
            break
        list_of_genre.append(genre)

    conditions = []
    params = []
    for genre in list_of_genre:
        conditions.append("genre LIKE %s")
        params.append(f"%{genre}%")

    query = "SELECT * FROM anime_info WHERE " + " AND ".join(conditions)
    query += "ORDER BY score DESC"
    df = pd.read_sql(query, db, params=tuple(params))
    print(df.head(10))

#To sort anime based on MAL score
def find_anime_score():
    print(" ")
    asc_desc=int(input("Enter '1' to see the highest scored anime and '2' to see the lowest scored anime: "))
    limit=int(input("Enter the number of rows you wish to see: "))
    if asc_desc==1:
        query="""SELECT *
                 FROM anime_info
                 ORDER BY score DESC
                 LIMIT %s
              """
    elif asc_desc==2:
        query="""SELECT *
                 FROM anime_info
                 WHERE score IS NOT NULL
                 ORDER BY score ASC
                 LIMIT %s
              """
    df=pd.read_sql(query, db, params=(limit,))
    print(df) 

#To sort anime based on rank decided by MAL users
def find_anime_rank():
    print(" ")
    asc_desc=int(input("Enter '1' to see the highest ranked anime and '2' to see the lowest ranked anime: "))
    limit=int(input("Enter the number of rows you wish to see: "))
    if asc_desc==1:
        query="""SELECT ai.id,ai.title,ai.genre,score,ranking,popularity
                 FROM anime_info ai
                 JOIN pop_and_rank par
                 USING (id)
                 WHERE ranking IS NOT NULL
                 ORDER BY ranking ASC
                 LIMIT %s
              """
    elif asc_desc==2:
        query="""SELECT ai.id,ai.title,ai.genre,score,ranking,popularity
                 FROM anime_info ai
                 JOIN pop_and_rank par
                 USING (id)
                 ORDER BY ranking DESC
                 LIMIT %s
              """
    df=pd.read_sql(query, db, params=(limit,))
    print(df)

#To sort anime based on popularity decided by MAL users
def find_anime_pop():
    print(" ")
    asc_desc=int(input("Enter '1' to see the most popular anime and '2' to see the least popular anime: "))
    limit=int(input("Enter the number of rows you wish to see: "))
    if asc_desc==1:
        query="""SELECT ai.id,ai.title,ai.genre,score,ranking,popularity
                 FROM anime_info ai
                 JOIN pop_and_rank par
                 USING (id)
                 ORDER BY popularity ASC
                 LIMIT %s
              """
    elif asc_desc==2:
        query="""SELECT ai.id,ai.title,ai.genre,score,ranking,popularity
                 FROM anime_info ai
                 JOIN pop_and_rank par
                 USING (id)
                 ORDER BY popularity DESC
                 LIMIT %s
              """
    df=pd.read_sql(query, db, params=(limit,))
    print(df)

#While loop to prompt users until they exit
while choice>0 and choice<6:
    print(" ")
    print("Select the task you want to perform:")
    print("1.Find anime id")
    print("2.Find anime titles according to genres")
    print("3.Sort anime titles based on score")
    print("4.Sort anime titles based on rank")
    print("5.Sort anime titles based on popularity")
    print("6.Exit")
    choice=int(input("Enter your choice: "))

    match_choice(choice)
