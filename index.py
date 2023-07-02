from Mysql_connect import Connection, executeDatabaseCommand
from Ws_partidas import getPartida
from Ws_times import getTimes
from Ws_campeonato import getCampeonato

def verificarCampeonato(Campeonato, Divisao, Ano):
    sql = ("select id, Campeonato, Divisao, Ano from campeonatos");
    Connection.execute(sql);
    campeonatosCadastradosRaw = Connection.fetchall();
    
    for item in campeonatosCadastradosRaw:  
        if(item[1].lower() == Campeonato.lower() and item[2].lower() == Divisao.lower() and str(item[3]) == str(Ano)):
            return [True, item[0]]
    return [False, 0]   

def verificarTime(Time):
    sql = ("select id, time from times");
    Connection.execute(sql);
    timesCadastradosRaw = Connection.fetchall();
    
    for item in timesCadastradosRaw:
        if(item[1].lower() == Time.lower()):
            return [True, item[0]]
    return [False, 0]

def cadastrarCampeonato(anoCampeonato):
    dados = getCampeonato(anoCampeonato);
    existeCampeonato = verificarCampeonato(dados[0], dados[1], dados[2])

    if(existeCampeonato[0]):
        print(dados[0]+" - "+dados[1]+" - "+dados[2] + " já cadastrado!");
    else:
        sql = ("INSERT INTO campeonatos (campeonato, divisao, ano, ativo) VALUES (%s, %s, %s, %s)");
        values = (dados[0], dados[1], dados[2], 1);

        Connection.execute(sql, values)
        executeDatabaseCommand();
    
def cadastrarTimes(anoCampeonato):
    times = getTimes(anoCampeonato);

    for time in times:
        existeTime = verificarTime(time);
    
        if(existeTime[0]):
            print(time + " já cadastrado!")
        else:
            apelidoRaw = time.split(' - ');
            apelido = apelidoRaw[0].replace(' Saf','').replace(' S.a.f.','')
            sql = ("INSERT INTO times (time, ativo, timeApelido) VALUES (%s, %s, %s)");
            values = (time, 1, apelido);

            Connection.execute(sql, values)
            executeDatabaseCommand(); 
      
cadastrarTimes(2023)     
#cadastrarCampeonato(2023)
#print(verificarTime('Flamengo'))
        
'''
if(hasattr(test, 'mandante_placar')):
    print(test.partida_numero);
    print(test.mandante_nome);
    print(test.mandante_placar);
    print(test.visitante_nome);
    print(test.visitante_placar);  
    print(test.partida_local);
    print(test.partida_data)
    print(test.msg)
    print(test.resultado_valido)
    print("MA: " + str(test.mandante_cartoes_amarelos)+" | VA: "+ str(test.visitante_cartoes_amarelos))
    print("MV: " + str(test.mandante_cartoes_vermelhos)+" | VV: "+ str(test.visitante_cartoes_vermelhos))
'''