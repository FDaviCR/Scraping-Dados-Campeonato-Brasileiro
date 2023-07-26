from tkinter import messagebox
from tkinter import Tk, ttk, Menu, Text
from ttkbootstrap import Style

from Functions.index import cadastrarCampeonato

anos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

def openFormCampeonatos():
    frameForm.pack(padx=20, pady=40)
    frameOptions.pack_forget()
    
def closeFormCampeonatos():
    frameForm.pack_forget()

style = Style(theme='superhero')
app = style.master

app.title("App - Campeonatos")
app.minsize(530, 300)
app.maxsize(1000, 800)

# Frames onde estão contidos os elementos em tela
frameWindow = ttk.Frame(borderwidth=2, relief='solid')
frameTitle = ttk.Frame(frameWindow)
frameOptions = ttk.Frame(frameWindow)
frameForm = ttk.Frame(frameWindow)

# Elementos do titulo exibido em tela
titulo = ttk.Label(frameTitle, text="Scraping de Dados de Campeonatos CBF", font=('Arial', 20))
titulo.grid(row=0, column=0, padx=10, pady=10)

# Botões para abertura dos forms de cadastros
cadastroCampeonatos = ttk.Button(frameOptions, text='Cadastrar Campeonatos', width=50, command=openFormCampeonatos)
cadastroCampeonatos.grid(row=0, column=0, pady=10)

cadastroTimes = ttk.Button(frameOptions, text='Cadastrar Times', width=50)
cadastroTimes.grid(row=1, column=0, pady=10)

cadastroPartidas = ttk.Button(frameOptions, text='Cadastrar Times', width=50)
cadastroPartidas.grid(row=2, column=0, pady=10)

# Elementos do form
labelAno = ttk.Label(frameForm, text='Escolha o ano: ', font=(None, 10))
labelAno.grid(row=1, column=0, padx=10, pady=5)

comboAno = ttk.Combobox(frameForm, values=anos, font=(None, 10), width=40)
comboAno.set(2023)
comboAno.grid(row=1, column=1, padx=10, pady=5)

frameWindow.pack(padx=20, pady=10)
frameTitle.pack(padx=20, pady=10)
frameOptions.pack(padx=20, pady=40)

app.mainloop()