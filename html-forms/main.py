from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

form_data = {}


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        user_name = request.form["username"]
        password = request.form["userpass"]
        form_data["username"] = user_name
        form_data["password"] = password
        return redirect(url_for('loging'))
        # return redirect(request.url)
    else:
        return render_template("index.html")


@app.route('/loging')
def loging():
    return render_template("loging.html", data=form_data["username"])


# action="{{ url_for('loging') }}"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
