from urllib import response
from flask import Flask, render_template, redirect, request
import datetime
from urllib.request import urlopen
from urllib.parse import urlencode

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

        #update data for tray1
        
        #get last data for tray1
        pH1 = 7
        moisture1 = 10
        time1 = datetime.datetime.now()

        #get last data for tray2
        pH2 = 7
        moisture2 = 10
        time2 = datetime.datetime.now()

        #output data to thingspeak
        api = "MAM1MDSXCO7T18KT"
        params = {1:pH1, 2:moisture1, "api_key":api}
        params = urlencode(params)
        url = "https://api.thingspeaks.com/update?" + params
        response = urlopen(url)
        #print(response.status, response.reason)
    else:
        #move to tray2

        #collect data for tray2

        #update data for tray2

        #get last data for tray1
        pH1 = 7
        moisture1 = 10
        time1 = datetime.datetime.now()

        #get last data for tray2
        
        pH2 = 7
        moisture2 = 10
        time2 = datetime.datetime.now()

        #output data to thingspeak
        api = "MAM1MDSXCO7T18KT"
        params = {3:pH2, 4:moisture2, "api_key":api}
        params = urlencode(params)
        url = "https://api.thingspeaks.com/update?" + params
        response = urlopen(url)

    return redirect(request.referrer)

#background process happening without any refreshing
@app.route('/button_test')
def button_test():
    print ("Hello")
    return redirect(request.referrer)
