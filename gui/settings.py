from tkinter import *
import game

class Application(Frame):

    def __init__ (self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def bbbbb(self):
        self.xr = self.ball_numbers.get()
        print("printing...", self.xr)
        return self.xr        

    def create_widgets(self):

        self.ball_numbers = IntVar()

        Label(self,text = "Select how many balls you wish to play:").grid()

        Radiobutton(self, text = "1 Ball", variable = self.ball_numbers, value = 1, command = self.bbbbb).grid ()
        Radiobutton(self, text = "2 Balls", variable = self.ball_numbers, value = 2, command = self.bbbbb).grid ()
        Radiobutton(self, text = "3 Balls", variable = self.ball_numbers, value = 3, command = self.bbbbb).grid ()


settings_window = Tk()
settings_window.title(" THE BOUNCER  -  Settings")
settings_window.geometry("600x600")
app = Application(settings_window)
settings_window.mainloop()