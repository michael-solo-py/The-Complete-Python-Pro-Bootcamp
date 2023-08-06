import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABESE_URL', 'sqlite:///user_comments.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, user_email, password, comment):
        self.username = username
        self.user_email = user_email
        self.password = password
        self.comment = comment


@app.route('/')
def index():
    users = UserComments.query.order_by(UserComments.date_posted.desc()).all()
    count_comments = UserComments.query.count()
    return render_template('index.html', users=users, count_comments=count_comments)


@app.route('/delete', methods=['POST', "GET"])
def delete():
    if request.method == "POST":
        user_ID = request.form['user_ID']

        delete_comment = UserComments.query.get(user_ID)
        db.session.delete(delete_comment)
        db.session.commit()
    return render_template('delete.html')


@app.route('/update', methods=['POST', "GET"])
def update():
    if request.method == "POST":
        user_id = request.form['user_id']
        update_name = request.form['new_name']

        update_user = UserComments.query.get(user_id)
        if update_name:
            update_user.username = update_name
            db.session.commit()

    return render_template('update.html')


@app.route('/last_five')
def last_five():
    last_5 = UserComments.query.order_by(UserComments.date_posted.desc()).limit(5).all()
    return render_template('last_five.html', last_5=last_5)


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
        user_email = request.form['email']

        # Fetch the user from the database
        user = UserComments.query.filter_by(username=username, user_email=user_email).first()
        if len(user.comment) > 1:
            new_comment = UserComments(username=username, password=user.password, user_email=user_email,
                                       comment=comment)
            db.session.add(new_comment)
            db.session.commit()
        else:
            user.comment = comment
            db.session.commit()

    users = UserComments.query.all()
    return render_template("add_comment.html", users=users)


@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        input_email = request.form['search_email']
        search_comment = UserComments.query.filter(or_(UserComments.user_email.like(f'%{input_email}%'),
                                                       UserComments.comment.like(f'%{input_email}%'))).all()
        print(search_comment)
        return render_template('search.html', search_comment=search_comment)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
