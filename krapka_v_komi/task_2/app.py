import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABESE_URL', 'sqlite:///comments.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['POST', 'GET'])
def index():
    with app.app_context():
        if request.method == "POST":
            username = request.form['username']
            email = request.form['email']
            comment = request.form['comment']

            new_comment = Comments(username=username, user_email=email, comment=comment)
            db.session.add(new_comment)
            db.session.commit()

        comments = Comments.query.all()
    return render_template('index.html', comments=comments)


if __name__ == "__main__":
    app.run(debug=True)
