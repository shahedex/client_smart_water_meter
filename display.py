import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.IN)
counter = 0;

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding


font = ImageFont.load_default()

while True:
        inputval = gpio.input(27)
        if inputval == False:
            with open('onemindata.txt','r') as f:
                lines = f.read().splitlines()
                last_line = lines[-1]
                data = last_line.split(",")
                pulse = data[0]
                datetime = data[1].split(" ")
                times = datetime[1]
                dates = datetime[0]
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x,top),"Last Recorded Data",font=font,fill=255)
            disp.clear()
            draw.text((x,top+20),"Data:"+str(pulse),font=font,fill=255)
            disp.clear()
            draw.text((x,top+30),"Time:"+str(times),font=font,fill=255)
            disp.clear()
            draw.text((x,top+40),"Date:"+str(dates),font=font,fill=255)
            disp.clear()
            disp.image(image)
            disp.display()
            disp.clear()
            time.sleep(10.0)
            disp.begin()
            disp.clear()
            disp.display()
            width = disp.width
            height = disp.height
            image = Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            while inputval == False:
                time.sleep(0.5)
                inputval = gpio.input(27)
