from tkinter import messagebox
from tkinter import Tk, ttk, Menu, Text
from ttkbootstrap import Style

style = Style(theme='superhero')
app = style.master

app.title("App - Campeonatos")
app.minsize(530, 300)
app.maxsize(1000, 800)

# Frames onde estão contidos os elementos em tela
frameWindow = ttk.Frame(borderwidth=2, relief='solid')
frameTitle = ttk.Frame(frameWindow)
frameForm = ttk.Frame(frameWindow)

# Elementos do titulo exibido em tela
titulo = ttk.Label(frameTitle, text="Scraping de Dados de Campeonatos CBF", font=('Arial', 20))
titulo.grid(row=0, column=0, padx=10, pady=10)

cadastroCampeonatos = ttk.Button(frameForm, text='Cadastrar Campeonatos', width=50)
cadastroCampeonatos.grid(row=0, column=0, pady=10)

cadastroTimes = ttk.Button(frameForm, text='Cadastrar Times', width=50)
cadastroTimes.grid(row=1, column=0, pady=10)

cadastroPartidas = ttk.Button(frameForm, text='Cadastrar Times', width=50)
cadastroPartidas.grid(row=2, column=0, pady=10)


frameWindow.pack(padx=20, pady=10)
frameTitle.pack(padx=20, pady=10)
frameForm.pack(padx=20, pady=40)

app.mainloop()