from Tkinter import *
import time
import RPi.GPIO as GPIO




t = Tk()

HEIGHT = 700
WIDTH = 800
canvas = Canvas(t,height=HEIGHT,width=WIDTH).pack()

background_image = PhotoImage(file='landscape.png')
background_label = Label(t, image=background_image)
background_label.place(relwidth=1, relheight=1)

labeltext = Label(canvas,text="RFID", font='Helvetica 18 bold')
labeltext.place(relx=0.5, rely=0.05,relwidth=1, relheight=0.25,anchor='n')
lower_frame = Frame(t, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.15, anchor='n')
label = Label(lower_frame)
label.place(relwidth=1, relheight=1)
button = Button( t,text="Summit", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.15)

t.mainloop()

