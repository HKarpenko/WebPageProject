from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/start')
def start():
    return render_template("start.html")

@app.route('/login', methods=["GET","POST"])
def login():
    
    return render_template("start.html")

if __name__ == '__main__':
    app.run()