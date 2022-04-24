from flask import Flask, render_template, redirect, request
from datetime import datetime

#init flask application
app = Flask(__name__)


@app.route('/')
def index():
    time1 = str(datetime.datetime.now())
    time2 = str(datetime.datetime.now())
    pH1 = -1
    pH2 = -2
    moisture1 = 0
    moisture2 = 0
    return render_template('index.html', time1, time2, pH1, pH2, moisture1, moisture2)

if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=True, port=5000)


#background process happening without any refreshing
@app.route('/button_test')
def button_test():
    print ("Hello")
    return redirect(request.referrer)