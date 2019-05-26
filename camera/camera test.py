from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button

camera = PiCamera()
button = Button(17)
now = datetime.now()

filename =''

def take_photo():
    global filename
    filename = "fff"
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/{0}".format(filename))
    camera.stop_preview()

button.when_pressed = take_photo()    
