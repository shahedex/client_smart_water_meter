import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as gpio
import urllib.request as req

device_id = '2'

while True:
                with open('onemindata.txt', 'r') as f:
                    lines = f.read().splitlines()
                    last_line = lines[-1]
                    data = last_line.split(",")
                    pulse = data[0]
                    datetime = data[1].replace(" ","%20")
                    urlstring = 'http://smartmeter.herokuapp.com/data/id/'+device_id+'/datetime/'+datetime+'/pulse/'+pulse
                    print(urlstring)
                    page = req.urlopen(urlstring)
                    print("Data Uploaded...")
                    time.sleep(60.0)
                
