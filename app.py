from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/start')
def start():
    return render_template("start.html")


@app.route('/login', methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["uname"] != "admin":
            error = "Permission denied."
        elif request.form["uname"] == "" and request.form["psw"] == "":
            error = "Empty fields"
        else:
            return redirect(url_for("start"))
    return render_template("login.html", error=error)


if __name__ == '__main__':
    app.run(debug = True)