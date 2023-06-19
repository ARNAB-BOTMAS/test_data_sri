import sqlite3

conn = sqlite3.connect("person_data.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE users (
    id VARCHAR(50),
    name VARCHAR(100),
    email VARCHAR(100),
    gender VARCHAR(10),
    password VARCHAR(100)
)"""
cursor.execute(sql_query)