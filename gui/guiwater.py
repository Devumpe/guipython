
from tkinter import *
from PIL import ImageTk, Image
root = Tk()

canv = Canvas(root, width=800, height=800, bg='white')
canv.grid(row=2, column=3)
photo = Image.open("correct.jpg")

photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
canv.create_image(130, 20, anchor=NW, image=img)

keyframe = Frame(canv, bg='#80c1ff', background="blue")
keyframe.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.10, anchor='n')
label = Label(keyframe,text="keyroom:")

button = Button( root,text="Summit", font=40, command=lambda: controller.show_frame("guirfid"))
button.place(relx=0.4, rely=0.70, relheight=0.1, relwidth=0.15)


root.mainloop()
