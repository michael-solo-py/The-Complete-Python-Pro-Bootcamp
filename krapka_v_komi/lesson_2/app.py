from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        if request.method == 'POST':
            name = request.form['name']
            price = float(request.form['price'])
            description = f'description {name}  price  {price}'
            new_product = Product(name=name, price=price, description=description)
            db.session.add(new_product)
            db.session.commit()

    products = Product.query.all()
    return render_template('index.html', products=products)


if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True, port=3000, host="127.0.0.1")