from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/button_test')
def button_test():
    print ("Hello")
    return redirect(request.referrer)