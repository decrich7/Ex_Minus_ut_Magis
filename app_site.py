from flask import Flask, render_template, redirect, url_for, request, flash
import psycopg2
from data import config

app = Flask(__name__)
app.secret_key = "super"


def sql_connection():
    try:
        con = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="24651asd",
            host="127.0.0.1",
            port="5432"
        )
        return con
    except Exception as ex:
        print(ex)


@app.route('/admin/<login>', methods=['POST', 'GET'])
def index(login):
    con = sql_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Users ;")
    rows = cur.fetchall()
    if request.method == "POST":
        delete_id = request.form['lol']
        id_user_delete = request.form['id']
        if delete_id != ' ':
            cur.execute(f"UPDATE Users SET tovar=0, id_buy=0 WHERE id_buy='{delete_id[1::]}'")
            con.commit()
        elif id_user_delete != ' ':
            cur.execute('DELETE FROM Users WHERE id=%s', id_user_delete[1::])
            con.commit()
        return render_template("index.html", rows=rows)
    else:
        return render_template("index.html", rows=rows)


@app.route('/', methods=['POST', 'GET'])
def enter_panel():
    if request.method == "POST":
        login = request.form['loginnn']
        password = request.form['passwwword']
        if login == config.LOGIN and password == config.PASSWORD:
            return redirect('/admin/<login>')
        else:
            return render_template('kekich.html')

    else:
        return render_template("kekich.html")


if __name__ == "__main__":
    app.run(debug=True)
