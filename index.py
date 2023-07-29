from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style

from Functions.index import cadastrarCampeonato

anos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
campeonatos = ['Campeonato Brasileiro de Futebol']
divisoes = ['Série A','Série B','Série C']

def openFormCampeonatos():
    app.title('Cadastro de Campeonato Brasileiro')
    frameFormCampeonato.pack(padx=20, pady=40)
    frameOptions.pack_forget()
    
def openFormTimes():
    app.title('Cadastro de Times')
    frameFormTime.pack(padx=20, pady=40)
    frameOptions.pack_forget()
    
def openFormPartidas():
    app.title('Cadastro de Partidas')
    frameFormPartida.pack(padx=20, pady=40)
    frameOptions.pack_forget()
    
def closeForm():
    app.title("App - Campeonatos")
    frameFormCampeonato.pack_forget()
    frameFormTime.pack_forget()
    frameFormPartida.pack_forget()
    frameOptions.pack(padx=20, pady=40)
    
def cadastrarCampeonato():
    messagebox.showinfo(title='Mensagem de retorno', message='Cadastro de Campeonato')
    
def cadastrarTime():
    messagebox.showinfo(title='Mensagem de retorno', message='Cadastro de Time')
    
def cadastrarPartidas():
    messagebox.showinfo(title='Mensagem de retorno', message='Cadastro de PArtidas')

# Configurações iniciais de tela
style = Style(theme='superhero')
app = style.master

app.title("App - Campeonatos")
app.minsize(530, 300)
app.maxsize(1000, 800)

# Frames onde estão contidos os elementos em tela
frameWindow = ttk.Frame(borderwidth=2, relief='solid')
frameTitle = ttk.Frame(frameWindow)
frameOptions = ttk.Frame(frameWindow)
frameFormCampeonato = ttk.Frame(frameWindow)
frameFormTime = ttk.Frame(frameWindow)
frameFormPartida = ttk.Frame(frameWindow)

# Elementos do titulo exibido em tela
titulo = ttk.Label(frameTitle, text="Scraping de Dados de Campeonatos CBF", font=('Arial', 20))
titulo.grid(row=0, column=0, padx=10, pady=10)

# Botões para abertura dos forms de cadastros
cadastroCampeonatos = ttk.Button(frameOptions, text='Cadastrar Campeonatos', width=50, command=openFormCampeonatos)
cadastroCampeonatos.grid(row=0, column=0, pady=10)

cadastroTimes = ttk.Button(frameOptions, text='Cadastrar Times', width=50, command=openFormTimes)
cadastroTimes.grid(row=1, column=0, pady=10)

cadastroPartidas = ttk.Button(frameOptions, text='Cadastrar Partidas', width=50, command=openFormPartidas)
cadastroPartidas.grid(row=2, column=0, pady=10)

# Elementos do form de cadastro de campeonato
labelAno = ttk.Label(frameFormCampeonato, text='Escolha o ano: ', font=(None, 10), width=20)
labelAno.grid(row=1, column=0, padx=10, pady=5)

comboAno = ttk.Combobox(frameFormCampeonato, values=anos, font=(None, 10), width=20)
comboAno.set(2023)
comboAno.grid(row=1, column=1, padx=10, pady=5)

buttonVoltar = ttk.Button(frameFormCampeonato, text='Voltar', command=closeForm, width=20)
buttonVoltar.grid(row=3, column=0, padx=10, pady=10)

buttonCadastrar = ttk.Button(frameFormCampeonato, text='Cadastrar', command=cadastrarCampeonato, width=20)
buttonCadastrar.grid(row=3, column=1, padx=10, pady=10)

# Elementos do form de cadastro de times
labelAno = ttk.Label(frameFormTime, text='Escolha o ano: ', font=(None, 10), width=20)
labelAno.grid(row=1, column=0, padx=10, pady=5)

comboAno = ttk.Combobox(frameFormTime, values=anos, font=(None, 10), width=20)
comboAno.set(2023)
comboAno.grid(row=1, column=1, padx=10, pady=5)

buttonVoltar = ttk.Button(frameFormTime, text='Voltar', command=closeForm, width=20)
buttonVoltar.grid(row=3, column=0, padx=10, pady=10)

buttonCadastrar = ttk.Button(frameFormTime, text='Cadastrar', command=cadastrarTime, width=20)
buttonCadastrar.grid(row=3, column=1, padx=10, pady=10)

# Elementos do form de cadastro e atualização de partidas
labelAno = ttk.Label(frameFormPartida, text='Escolha o ano: ', font=(None, 10))
labelAno.grid(row=1, column=0, padx=10, pady=5)

comboAno = ttk.Combobox(frameFormPartida, values=anos, font=(None, 10), width=40)
comboAno.set(2023)
comboAno.grid(row=1, column=1, padx=10, pady=5)

labelCampeonato = ttk.Label(frameFormPartida, text='Escolha o campeonato: ', font=(None, 10))
labelCampeonato.grid(row=2, column=0, padx=10, pady=5)

comboCampeonato = ttk.Combobox(frameFormPartida, values=campeonatos, font=(None, 10), width=40)
comboCampeonato.set('Campeonato Brasileiro de Futebol')
comboCampeonato.grid(row=2, column=1, padx=10, pady=5)

labelDivisao = ttk.Label(frameFormPartida, text='Escolha a divisão: ', font=(None, 10))
labelDivisao.grid(row=3, column=0, padx=10, pady=5)

comboDivisao = ttk.Combobox(frameFormPartida, values=divisoes, font=(None, 10), width=40)
comboDivisao.set('Série A')
comboDivisao.grid(row=3, column=1, padx=10, pady=5)

buttonVoltar = ttk.Button(frameFormPartida, text='Voltar', command=closeForm, width=20)
buttonVoltar.grid(row=4, column=0, padx=10, pady=10)

buttonCadastrar = ttk.Button(frameFormPartida, text='Cadastrar', command=cadastrarPartidas, width=20)
buttonCadastrar.grid(row=4, column=1, padx=10, pady=10)

# Inicialização dos Frames principais
frameWindow.pack(padx=20, pady=10)
frameTitle.pack(padx=20, pady=10)
frameOptions.pack(padx=20, pady=40)

app.mainloop()