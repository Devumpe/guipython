from tkinter import *
t = Tk()

HEIGHT = 700
WIDTH = 800
canvas = Canvas(t,height=HEIGHT,width=WIDTH).pack()
background_image = PhotoImage(file='landscape.png')
background_label = Label(t, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = Frame(t,bg='#80c1ff')
frame.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.8, anchor='n')

button = Button( t,text="Summit", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.15)


t.mainloop()