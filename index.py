from tkinter import messagebox
from tkinter import Tk, ttk, Button, Text
from ttkthemes import ThemedTk
from ttkbootstrap import Style

#app = Tk()
#app = ThemedTk(theme='equilux')

style = Style(theme='superhero')
app = style.master

app.title("App - Campeonatos")
app.minsize(500, 400)
#app.maxsize(1000, 800)

frameWindow = ttk.Frame()
frameTitle = ttk.Frame(frameWindow)
frameForm = ttk.Frame(frameWindow)

titulo = ttk.Label(frameTitle, text="Titulo")
titulo.grid(row=0, column=0, padx=10, pady=10)
'''
style = ttk.Style()
style.configure('TButton', font=('Arial', 30))

frame1 = ttk.Frame()

b2 = ttk.Button(frame1 ,text='Python')
b2.grid(row=0, column=0, padx=10, pady=10)

entrada = Text()
entrada.pack(padx=10, fill='both', expand='yes')

b1 = ttk.Button(text='TESTE')
b1.pack(fill='both')

frame1.pack()
'''
frameWindow.pack()
frameForm.pack()
frameTitle.pack()
#b2.pack(padx=20, pady=50)

app.mainloop()