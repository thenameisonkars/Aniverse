#This is the first offocial file of the Anime-Recommendation-System project that I am working on
#Aim of this file is to import the list of anime MAL ids from a csv file I found on kaggle and create a database of our own
#using the Jikan API

#Setting up a database where we can store our data

import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="minakshi*",
    database="Database_Anime"      
    )
mycursor=db.cursor()
create_database="CREATE DATABASE Database_Anime"

#mycursor.execute(create_database)
#We have now created a database successfully called Database_Anime
#Next task is to create tables for storing anime info
#We will use only this file to create tables,etc

table1="CREATE TABLE list_of_ids (id INT PRIMARY KEY NOT NULL, title VARCHAR(200) NOT NULL)"

mycursor.execute(table1)

table2="CREATE TABLE anime_info (id INT PRIMARY KEY NOT NULL, title VARCHAR(200) NOT NULL,genre VARCHAR(200) NOT NULL, score FLOAT NOT NULL)"

mycursor.execute(table2)

table3="CREATE TABLE pop_and_rank (id INT PRIMARY KEY NOT NULL, title VARCHAR(200) NOT NULL, ranking INT NOT NULL, popularity INT NOT NULL)"

mycursor.execute(table3)

table4="CREATE TABLE test1 (id INT PRIMARY KEY NOT NULL, title VARCHAR(200) NOT NULL,genre VARCHAR(200) NOT NULL, score FLOAT NOT NULL)"

#mycursor.execute(table4)

table5="CREATE TABLE test2 (id INT PRIMARY KEY NOT NULL, title VARCHAR(200) NOT NULL, ranking INT NOT NULL, popularity INT NOT NULL)"

#mycursor.execute(table5)