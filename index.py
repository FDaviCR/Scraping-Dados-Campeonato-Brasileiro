from Mysql_connect import Connection, executeDatabaseCommand
from Ws_partidas import getPartida
from Ws_times import getTimes
from Ws_campeonato import getCampeonato

def verificarCampeonato(Campeonato, Divisao, Ano):
    sql = ("select id, Campeonato, Divisao, Ano from campeonatos");
    Connection.execute(sql);
    campeonatosCadastradosRaw = Connection.fetchall();
    
    for item in campeonatosCadastradosRaw:  
        print(item[1].lower() +'='+ Campeonato.lower() +'---'+ item[2].lower() +'='+ Divisao.lower() +'---'+ str(item[3]) +'='+ str(Ano))  
        if(item[1].lower() == Campeonato.lower() and item[2].lower() == Divisao.lower() and str(item[3]) == str(Ano)):
            return [True, item[0]]
    return [False, 0]   

def cadastrarCampeonato(anoCampeonato):
    dados = getCampeonato(anoCampeonato);
    existeCampeonato = verificarCampeonato(dados[0], dados[1], dados[2])
    print(dados[0]+" - "+dados[1]+" - "+dados[2]);
    '''
    sqlCheck = ("select Campeonato, Divisao, Ano from campeonatos");
    Connection.execute(sqlCheck);
    campeonatosCadastradosRaw = Connection.fetchall();
    campeonatosCadastrados = [];
    
    for campeonato in campeonatosCadastradosRaw:
        campeonatosCadastrados.append(campeonato[0].lower()+campeonato[1].lower()+str(campeonato[2]));
      
    if((dados[0].lower()+dados[1].lower()+str(dados[2])) in campeonatosCadastrados):
        print(dados[0]+" - "+dados[1]+" - "+dados[2] + " já cadastrado!");
    '''  
    print(existeCampeonato)
    if(existeCampeonato[0]):
        print(dados[0]+" - "+dados[1]+" - "+dados[2] + " já cadastrado!");
    else:
        sql = ("INSERT INTO campeonatos (campeonato, divisao, ano, ativo) VALUES (%s, %s, %s, %s)");
        values = (dados[0], dados[1], dados[2], 1);

        Connection.execute(sql, values)
        executeDatabaseCommand();
    
def cadastrarTimes(anoCampeonato):
    times = getTimes(anoCampeonato);
    sqlCheck = ("select time from times");
    Connection.execute(sqlCheck);
    timesCadastradosRaw = Connection.fetchall();
    timesCadastrados = [];
    
    for time in timesCadastradosRaw:
        timesCadastrados.append(time[0].lower());
    
    for time in times:
        if(time.lower() in timesCadastrados):
            print(time + " já cadastrado!")
        else:
            apelidoRaw = time.split(' - ');
            apelido = apelidoRaw[0].replace(' Saf','').replace(' S.a.f','')
            sql = ("INSERT INTO times (time, ativo, timeApelido) VALUES (%s, %s, %s)");
            values = (time, 1, apelido);

            Connection.execute(sql, values)
            executeDatabaseCommand();
        
#cadastrarTimes(2023)     
cadastrarCampeonato(2021)
#print(verificarCampeonato('Campeonato Brasileiro de Futebol', 'Série A', 2021))
        
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