from flask import Flask, render_template, redirect, request, send_file
import datetime

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
    return render_template('index.html', time1=time1, time2=time2, pH1=pH1, pH2=pH2, moisture1=moisture1, moisture2=moisture2)

if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=True, port=5000)

@app.route('/collectDataButton/<trayNum>')
def collectDataButton(trayNum):
    if trayNum == 1:
        #move to tray1
        #collect data for tray1
        pH1 = 7
        moisture1 = 10
        time1 = datetime.datetime.now()

        #get last data for tray2
        pH2 = 7
        moisture2 = 10
        time2 = datetime.datetime.now()
    else:
        #move to tray2
        #collect data for tray2
        pH2 = 7
        moisture2 = 10
        time2 = datetime.datetime.now()

        #get last data for tray1
        pH1 = 7
        moisture1 = 10
        time1 = datetime.datetime.now()

    render_template('index.html', time1=time1, time2=time2, pH1=pH1, pH2=pH2, moisture1=moisture1, moisture2=moisture2)

    return redirect(request.referrer)

#background process happening without any refreshing
# @app.route('/button_test')
# def button_test():
#     print ("Hello")
#     return redirect(request.referrer)

# @app.route('/downloadButton')
@app.route('/', methods=['POST'])
def downloadFile():
    # Export new data to csv
    ############################################################################TO DO
    print(request.form.get("data-start"))
    print(request.form.get("data-stop"))
    print(request.form.get("tray1-box"))
    print(request.form.get("tray2-box"))

    # print(request.form.get("textField"))

    # Return data
    path = "./plantDataExport.csv"
    return send_file(path, as_attachment=True)

