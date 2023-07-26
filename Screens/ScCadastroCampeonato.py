from tkinter import messagebox
from tkinter import Tk, ttk, Menu, Text
from ttkbootstrap import Style

anos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

style = Style(theme='superhero')
app = style.master

app.title("Cadastrar Campeonato")
app.minsize(530, 300)
app.maxsize(1000, 800)

# Frames onde estão contidos os elementos em tela
frameWindow = ttk.Frame(borderwidth=2, relief='solid')
frameTitle = ttk.Frame(frameWindow)
frameForm = ttk.Frame(frameWindow, borderwidth=2, relief='solid')

# Elementos do titulo exibido em tela
titulo = ttk.Label(frameTitle, text="Cadastrar Campeonato", font=('Arial', 20))
titulo.grid(row=0, column=0, padx=10, pady=10)

# Elementos do form
labelAno = ttk.Label(frameForm, text='Escolha o ano: ', font=(None, 10))
labelAno.grid(row=1, column=0, padx=10, pady=5)

comboAno = ttk.Combobox(frameForm, values=anos, font=(None, 10), width=40)
comboAno.set(2023)
comboAno.grid(row=1, column=1, padx=10, pady=5)

buttonCadastrar = ttk.Button(frameForm, text='Cadastrar Campeonato')
buttonCadastrar.grid(row=4, column=1, padx=5, pady=10)

buttonVoltar = ttk.Button(frameForm, text='Voltar')
buttonVoltar.grid(row=8, column=1, padx=100, pady=40)

frameWindow.pack(padx=20, pady=10)
frameTitle.pack(padx=20, pady=10)
frameForm.pack(padx=20, pady=40)

app.mainloop()