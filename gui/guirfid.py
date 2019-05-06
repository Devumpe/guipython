from tkinter import *
from PIL import ImageTk, Image
root = Tk()

canv = Canvas(root, width=800, height=800, bg='white')
canv.grid(row=2, column=3)
photo = Image.open("w.jpg")

photo.resize((5, 5), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
canv.create_image(5, 5, anchor=NW, image=img)


mainloop()


