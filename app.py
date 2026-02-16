from flask import Flask, g
import sqlite3

DATABASE = 'database1.db'

#initialize app
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    db = get_db()
    cursor = db.cursor()
    sql = "SELECT * FROM Cars"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return str(rows)

if __name__ == '__main__':
    app.run(debug=True)