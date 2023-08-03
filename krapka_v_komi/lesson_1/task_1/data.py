import sqlite3

database = sqlite3.connect('data.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS mynotes (id INTEGER PRIMARY KEY, note TEXT, date DATE )")
database.commit()


def connect_db():
    database = sqlite3.connect('data.db')
    cursor = database.cursor()
    return database, cursor

