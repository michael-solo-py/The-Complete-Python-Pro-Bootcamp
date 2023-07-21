from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', post=response)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def show_the_post(id):
    get_post = None
    for index in response:
        if index['id'] == id:
            get_post = index
    return render_template('post.html', post=get_post)


if __name__ == "__main__":
    app.run(debug=True)
