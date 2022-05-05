from flask import Flask, render_template, redirect, request, send_file
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib import response
import Sensing.PlantTester as PlantTester
import pandas as pd
import RPi.GPIO as gpio
import time
import moving.xyaxis as xyaxis
import moving.zaxis as zaxis

gpio.setmode(gpio.BCM)
# Set up solenoid pins
solenoid1Pin = 5
solenoid2Pin = 6
gpio.setup(solenoid1Pin, gpio.OUT)
gpio.setup(solenoid2Pin, gpio.OUT)
z = zaxis.zaxis(step = 19, dir = 13)
xy = xyaxis.xyaxis()

#init flask application
app = Flask(__name__)

@app.route('/')
def index():
    # move to neutral position
    # move y up out of soil
    # pos = xy.current_pos()
    # x = pos[0]
    # y = pos[1]
    # xy.move(x, y-130)
    # move z towards gantry

    # move xy to neutral position


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
      app.run(host='0.0.0.0', debug=False, port=5000)
