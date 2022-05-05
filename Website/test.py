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