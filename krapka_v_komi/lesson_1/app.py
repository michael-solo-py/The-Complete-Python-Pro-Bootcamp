# from flask import Flask, render_template
# import sqlite3
# from random import randint
#
# app = Flask(__name__)
#
# # Simple data list for Dynamic Routing
# users = [
#     {"id": 1, "name": "Ivan"},
#     {"id": 2, "name": "Oleh"},
#     {"id": 3, "name": "Alex"}
# ]
#
# database = sqlite3.connect('data.db')
# cursor = database.cursor()
# database.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
# database.commit()
#
# # for i in range(100):
# #     name = f"Bob{i}"
# #     age = randint(14, 90)
# #     cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
# #
# # database.commit()
#
#
# # URL Building та роут для головної сторінки
# @app.route('/')
# def index():
#     return "Hello world in Flask!"
#
#
# # Templates та Render HTML
# @app.route('/hi/<name>')
# def hello_to_user(name):
#     return render_template('greeting.html', name=name)
#
#
# # Jinja2 and Template Inheritance
# @app.route('/about')
# def about():
#     return render_template('about.html', title='About Us', content='This is the about page.')
#
#
# @app.route('/user/<int:user_id>')
# def user_profile(user_id):
#     database = sqlite3.connect('data.db')
#     cursor = database.cursor()
#     cursor.execute('SELECT * FROM users')
#
#     users = cursor.fetchall()
#     database.commit()
#     for user in users:
#         if user['id'] == user_id:
#             return f"User Profile: {user['name']}"
#     return "User not found!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from data import connect_db

app = Flask(__name__)


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    database, cursor = connect_db()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == user_id:
            return f"User Profile: {user[1]}"

    return "User not found!"


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    database, cursor = connect_db()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    database.commit()
    return "User seved"


@app.route('/add_user', methods=['GET'])
def add_user_form():
    return render_template('add_user.html')


if __name__ == "__main__":
    app.run(debug=True)