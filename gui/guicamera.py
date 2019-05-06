import tkinter
from subprocess import Popen

t = tkinter.Tk()

HEIGHT = 700
WIDTH = 800
canvas = tkinter.Canvas(t,height=HEIGHT,width=WIDTH).pack()
frame = tkinter.Frame(t,bg='#80c1ff')
frame.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.8, anchor='n')

def start():
    import os
#    os.system("python test.py")
    Popen(["python", "guishow.py"])
    t.destroy()


button = tkinter.Button( t,text="Get Weather", font=40, command = start)
button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.15)


t.mainloop()