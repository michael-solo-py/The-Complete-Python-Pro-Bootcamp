from flask import Flask, render_template
from post import Post
import requests

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
post_arr = []
for item in response:
    post_obj = Post(item['id'], item['title'], item['subtitle'], item['body'])
    post_arr.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("add_user.html", all_posts=post_arr)


@app.route('/blog/<int:index>')
def write_post_main(index):
    requested_post = None
    for block in post_arr:
        if block.id == index:
            requested_post = block
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
