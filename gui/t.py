import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            label = tk.Label(self, text="Start Page", font=LARGE_FONT)
            label.pack(pady=10,padx=10)

            button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
            button.pack()

            button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
            button2.pack()

app = SeaofBTCapp()
app.mainloop()