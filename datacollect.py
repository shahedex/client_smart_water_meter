import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as gpio
import urllib.request as req
from datetime import datetime

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
counter = 0;

while True:
        file2 = open("onemindata.txt","a")
        inputval = gpio.input(17)
        datetime = datetime.now()
        dt = datetime.strftime('%m-%d-%Y %H:%M:%S')
        if inputval == False:
                file2.write(str(counter)+','+dt+'\n')
                file2.close()
                counter += 1
                time.sleep(0.2)
                while inputval == False:
                        inputval = gpio.input(17)
                        time.sleep(0.1)
