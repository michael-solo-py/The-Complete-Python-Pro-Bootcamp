import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABESE_URL', 'sqlite:///user_comments.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)
    comment = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, user_email, password, comment):
        self.username = username
        self.user_email = user_email
        self.password = password
        self.comment = comment


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/update')
def update():
    return render_template('update.html')


@app.route('/last_five')
def last_five():
    return render_template('last_five.html')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == "POST":
        username = request.form['username']
        user_email = request.form['email']
        password = request.form['password']
        new_user = UserComments(username=username, user_email=user_email, password=password, comment='')
        db.session.add(new_user)
        db.session.commit()

    return render_template("add_user.html")


@app.route('/add_comment', methods=['POST', 'GET'])
def add_comment():
    if request.method == "POST":
        comment = request.form['comment']
        username = request.form['username']
        email = request.form['email']

        # Fetch the user from the database
        user = UserComments.query.filter_by(username=username, user_email=email).first()
        if user:
            user.comment = comment
            db.session.commit()

    users = UserComments.query.all()
    return render_template("add_comment.html", users=users)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
