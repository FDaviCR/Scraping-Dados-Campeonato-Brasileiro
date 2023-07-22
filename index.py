import tkinter as tk
from tkinter import messagebox
'''
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

app = App()

app.master.title("App")
app.master.minsize(500, 400)
app.master.maxsize(1000, 800)
'''

app = tk.Tk()

app.title("App")
app.minsize(500, 400)
app.maxsize(1000, 800)

def helloCallBack():
   messagebox.showinfo("Dado", I.get())

tk.Label(app, text='TESTE').grid(row=0)
#L.pack(side = "left")

I = tk.Entry(app, text="Informe o ano")
I.grid(row=0, column=2)
#I.pack(side = "right")

tk.Button(app, text ="Hello", command = helloCallBack).grid(row=2, column=1)
#B.pack()

app.mainloop()