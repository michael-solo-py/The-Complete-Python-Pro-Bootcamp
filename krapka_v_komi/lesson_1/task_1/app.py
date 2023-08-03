from flask import Flask, render_template, request
from data import connect_db
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    date = datetime.date.today()
    if request.method == "POST":
        content = request.form
        name = content['name']
        note = content['note']
        database, cursor = connect_db()
        cursor.execute("INSERT INTO mynotes (note, date) VALUES (?, ?)", (note, date))
        database.commit()

        cursor.execute('SELECT * FROM mynotes ORDER BY id DESC LIMIT 10')
        rows = cursor.fetchall()
        print(rows)
        return render_template("index.html", rows=rows)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
