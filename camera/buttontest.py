from datetime import *
import time
from picamera import PiCamera
from time import sleep
from gpiozero import Button
from time import time

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





