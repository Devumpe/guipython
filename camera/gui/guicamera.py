import Tkinter
import picamera
from threading import Thread
import io
import sys
import time
from PIL import Image,ImageTk
import os

RQS_0=0
RQS_QUIT=1
RQS_CAPTURE=2
rqs=RQS_0
 
def camHandler():
    global rqs
    rqs = RQS_0
    
    camera = picamera.PiCamera()
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    #camera.rotation = 0
    camera.rotation = 270
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    camera.resolution = (1024, 768)
    camera.resolution = (400, 300)
    
    
    
    while rqs != RQS_QUIT:
        if rqs == RQS_CAPTURE:
            print("Capture")
            rqs=RQS_0
            timeStamp = time.strftime("%Y%m%d-%H%M%S")
            jpgFile='img_'+timeStamp+'.jpg'
            camera.resolution = (2592, 1944)    #set photo size
            camera.capture(jpgFile)
            camera.resolution = (400, 300)      #resume preview size
            labelCapVal.set(jpgFile)
        else:
            stream = io.BytesIO()
            camera.capture(stream,format='jpeg')
            stream.seek(0)
            tmpImage = Image.open(stream)
            tmpimg = ImageTk.PhotoImage(tmpImage)
            frame.configure(image = tmpimg)
            #sleep(0.5)
                
    print("Quit")        
    #camera.stop_preview()
    
    
    
def startCam():
    camThread = Thread(target=camHandler)
    camThread.start()
    
def quit():
    global rqs
    rqs=RQS_QUIT

    global t
    t.destroy()

def capture():
    global rqs
    rqs = RQS_CAPTURE
    labelCapVal.set("capturing")
    print("python guishow.py")

    
    
    
        
t = Tkinter.Tk()

HEIGHT = 700
WIDTH = 800

f = Tkinter.Frame(t)
f.place(relx=0.5,rely=0.02,relwidth=0.8,relheight=0.8,anchor='n')

frame = Tkinter.Label(f)
frame.pack(side="bottom",fill="both",expand = "yes")

labelCapVal = Tkinter.StringVar()
Tkinter.Label(frame, textvariable=labelCapVal).pack()

button = Tkinter.Button( t,text="Capture", font=40, command=capture)
button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.15)

startCam()
t.mainloop()
