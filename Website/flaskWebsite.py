from flask import Flask, render_template, redirect, request, send_file
import datetime
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib import response
import Sensing.PlantTester as PlantTester
import pandas as pd

#init flask application
app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_pickle("./plantData.pkl")
	#get last data for tray1
    pH1 = df.loc[df.Tray == 1].iloc[-1].pH
    moisture1 = df.loc[df.Tray == 1].iloc[-1].Moisture
    time1 = df.loc[df.Tray == 1].iloc[-1].Time

	#get last data for tray2
    pH2 = df.loc[df.Tray == 2].iloc[-1].pH
    moisture2 = df.loc[df.Tray == 2].iloc[-1].Moisture
    time2 = df.loc[df.Tray == 2].iloc[-1].Time
    return render_template('index.html', time1=time1, time2=time2, pH1=pH1, pH2=pH2, moisture1=moisture1, moisture2=moisture2)

if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=True, port=5000)

@app.route('/collectDataButton/<trayNum>')
def collectDataButton(trayNum):
    df = pd.read_pickle("./plantData.pkl")
    if trayNum == 1:
        
        #move to tray1

        #collect data for tray1
        pH1, temp, moisture1 = PlantTester.measure()
        #update data for tray1
        data={
            'Time':datetime.datetime.now(),
            'Tray':1,
            'Moisture':moisture1,
            'pH':pH1,
            'Temperature':temp
        }
        df = df.append(data, ignore_index=True)
        print(data)

        #output data to thingspeak
        api = "MAM1MDSXCO7T18KT"
        # params = {1:pH1, 2:moisture1, "api_key":api}
        # params = urlencode(params)
        # url = "https://api.thingspeak.com/update?" + params
        url = "https://api.thingspeak.com/update?api_key=" + api + "&field1=" + pH1 + "&field2=" + moisture1
        response = urlopen(url)
        print(response.status, response.reason)
    else:
        #move to tray2

        #collect data for tray2
        pH2, temp, moisture2 = PlantTester.measure()
        #update data for tray2
        data={
            'Time':datetime.datetime.now(),
            'Tray':1,
            'Moisture':moisture2,
            'pH':pH2,
            'Temperature':temp
        }
        df = df.append(data, ignore_index=True)
        

        #output data to thingspeak
        api = "MAM1MDSXCO7T18KT"
        # params = {3:pH2, 4:moisture2, "api_key":api}
        # params = urlencode(params)
        # url = "https://api.thingspeak.com/update?" + params
        url = "https://api.thingspeak.com/update?api_key=" + api + "&field3=" + pH2 + "&field4=" + moisture2
        response = urlopen(url)
        print(response.status, response.reason)


    
	# Read data from pickle
	#get last data for tray1
    pH1 = df.loc[df.Tray == 1].iloc[-1].pH
    moisture1 = df.loc[df.Tray == 1].iloc[-1].Moisture
    time1 = df.loc[df.Tray == 1].iloc[-1].Time

	#get last data for tray2
    pH2 = df.loc[df.Tray == 2].iloc[-1].pH
    moisture2 = df.loc[df.Tray == 2].iloc[-1].Moisture
    time2 = df.loc[df.Tray == 2].iloc[-1].Time
	
    # Save Data
    df.to_pickle("./plantData.pkl")

	# Display data
    # render_template('index.html', time1=time1, time2=time2, pH1=pH1, pH2=pH2, moisture1=moisture1, moisture2=moisture2)

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

