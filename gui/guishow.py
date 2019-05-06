from tkinter import *
from PIL import ImageTk, Image


t = Tk()
text = Text(t)

HEIGHT = 700
WIDTH = 800
canvas = Canvas(t,height=HEIGHT,width=WIDTH).pack()

labeltext = Label(canvas,text="Showdata", font='Helvetica 18 bold')
labeltext.place(relx=0.1, rely=0.05,relwidth=1, relheight=0.25,anchor='center')

frame = Frame(canvas,bg='#80c1ff')
frame.place(relx=0.5, rely=0.08, relwidth=0.5, relheight=0.5, anchor='n')
photo = Image.open("correct.jpg")
photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
label = Label(frame,image=img)
label.pack()

keyframe = Frame(canvas, bg='#80c1ff', bd=5)
keyframe.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.10, anchor='n')
label = Label(keyframe,text="keyroom:")
label.place(relwidth=1, relheight=1)

dateframe = Frame(canvas, bg='#80c1ff', bd=5)
dateframe.place(relx=0.5, rely=0.7, relwidth=0.8, relheight=0.10, anchor='n')
label = Label(dateframe,text="Date:")
label.place(relwidth=1, relheight=1)

summitbtn = Button( t,text="Summit", font=40, command=lambda: get_weather(entry.get()))
summitbtn.place(relx=0.3, rely=0.83, relheight=0.13, relwidth=0.15)
canclebtn = Button( t,text="Cancel", font=40, command=lambda: get_weather(entry.get()))
canclebtn.place(relx=0.6, rely=0.83, relheight=0.13, relwidth=0.15)
t.mainloop()



