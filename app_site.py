from flask import Flask, render_template, redirect, url_for, request
import psycopg2
import sqlite3
from sqlite3 import Error

#инициализация БД и flask app
app = Flask(__name__)
# con = psycopg2.connect(
#     database="Kekich", 
#     user="popusk", 
#     password="qwerty123", 
#     host="127.0.0.1", 
#     port="5000"
# )

# cur = con.cursor()

# cur.execute("""
#         CREATE TABLE IF NOT EXISTS Users (
#         id SERIAL PRIMARY KEY,
#         full_name VARCHAR(255) NULL,
#         username varchar(255) NULL,
#         telegram_id BIGINT NOT NULL UNIQUE 
#         );
#         """)
# con.commit()

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db', check_same_thread=False)

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS Users(id integer PRIMARY KEY, full_name varchar(255) NULL, username varchar(255) NULL, telegram_id integer NOT NULL)")

    con.commit()

con = sql_connection()
sql_table(con)

def sql_insert(con, entities):

    cursorObj = con.cursor()

    cursorObj.execute('INSERT OR REPLACE INTO Users(id, full_name, username, telegram_id) VALUES(?, ?, ?, ?)', entities)

    con.commit()

entities = (2, 'Andrew', 'loh', 800)

sql_insert(con, entities)
cursorObj = con.cursor()
#сам сайт)
@app.route('/', methods=['POST', 'GET'])
def index():
     cursorObj.execute("SELECT * FROM Users ;")
     rows = cursorObj.fetchall()
     return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)