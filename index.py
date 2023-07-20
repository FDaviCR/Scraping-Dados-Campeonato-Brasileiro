import tkinter as tk
#import tkMessageBox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

app = App()

app.master.title("App")
app.master.minsize(500, 400)
app.master.maxsize(1000, 800)

def helloCallBack():
   #tkMessageBox.showinfo(app, "Hello Python", "Hello World")
   print("Tst")


B = tk.Button(app, text ="Hello", command = helloCallBack)
B.pack()

app.mainloop()