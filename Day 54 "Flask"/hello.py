from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"""<b>{func(*args, **kwargs)}</b>"""

    return wrapper


def make_emphasize(func):
    def wrapper(*args, **kwargs):
        return f"""<em>{func(*args, **kwargs)}</em>"""

    return wrapper


def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"

    return wrapper


@app.route("/username/<name>/<int:number>")
@make_bold
@make_emphasize
@make_underlined
def hello_world(name, number):
    return f"Hello, {name}! You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
