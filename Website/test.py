from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=True, port=5000)

#background process happening without any refreshing
@app.route('/button_test')
def button_test():
    print ("Hello")
    return redirect(request.referrer)