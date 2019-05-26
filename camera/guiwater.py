from datetime import *
import time
from picamera import PiCamera
from time import sleep
from gpiozero import Button
from time import time
from tkinter import *

def camerameter():
    print("hello")
     #setup
     #button = Button(17)
    camera = PiCamera()
    today = datetime.now()
    date = today.strftime('%d%m%Y.%H%M%S')

     #camera
    camera.start_preview(alpha=190)
     #button.wait_for_press()
    sleep(5)
    camera.capture('/home/pi/camera/{0}.jpg'.format(date))
    camera.stop_preview()

     #txt
     #text_file = open('/home/pi/camera/data.txt','w')
    text_file = open('/home/pi/camera/data.txt','a')
    text_file.write('Date :'+date+'\n')
    text_file.close()

gui = Tk()
gui.geometry("1500x1000")
gui.title("Water meter")
mlabel = Label(text="Welcome to Watermetercamera!",bg="pink").pack()
mButton = Button(text="Submit",command=camerameter).pack()
gui.mainloop()