import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.messagebox import showinfo
from api import Cekilis

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('400x600')
        self.url = StringVar()
        self.winners = []
        
        
        self.urlEntry = ttk.Entry(self,width=30,textvariable = self.url)
        self.urlEntry.pack()
        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        self.label2 = ttk.Label(self, text='Kazananlar')
        self.label2.pack()
        

    def button_clicked(self):
        obj = Cekilis()
        self.winners = obj.requestVideo(str(self.url.get()),3)
        self.label3 = ttk.Label(self, text=self.winners)
        self.label3.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()