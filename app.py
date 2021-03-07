import os
import tempfile
from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename

import telebot

bot = telebot.TeleBot(token='1644959765:AAEn325HJiB-JFsMA5D2RqZoT3LBmoC1ZZg')
my_chat_id = 510305747

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)

"""
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(my_chat_id, "Hello")
"""

#@celery.task
def telegram_send(name="None",email="None",tel="None",order_type="None",order_message="None",files=None):
    message = "Имя пользователя: "+str(name)+"\n"
    message += "Email: " + str(email) + "\n"
    message += "Номер телефона: " + str(tel) + "\n"
    message += "Тип заказа: " + str(order_type) + "\n"
    message += "Главное сообщение: " + str(order_message)
    bot.send_message(my_chat_id, message)
    tempdirectory = tempfile.gettempdir()
    for file in files:
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(tempdirectory, filename))
            doc = open(os.path.join(tempdirectory, filename), 'rb')
            bot.send_document(my_chat_id, doc)
            doc.close()

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/order', methods=["POST"])
def upload_order():
    if request.method == "POST":
        if request.form["Name"] and request.form["Tel"] and request.form["Type"]:
            name = request.form["Name"]
            tel = request.form["Tel"]
            email = request.form["Email"]
            order_type = request.form["Type"]
            order_message = request.form["Message"]
            files = request.files.getlist("Files")
            telegram_send(name=name, tel=tel, email=email, order_type=order_type, order_message=order_message,
                          files=files)
            flash('Message were successfully sended')
    return redirect(request.url)


@app.route('/tattoos')
def tattoos():
    return render_template("tattoos.html")

@app.route('/sketches')
def sketches():
    return render_template("sketches.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True)