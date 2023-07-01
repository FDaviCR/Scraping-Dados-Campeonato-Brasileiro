from Mysql_connect import Connection, executeDatabaseCommand
from Ws_partidas import getPartida
from Ws_times import getTimes

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
            sql = ("INSERT INTO times (time, ativo, timeApelido) VALUES (%s, %s, %s)");
            values = (time, 1, time);

            Connection.execute(sql, values)
            executeDatabaseCommand();
        
cadastrarTimes(2023)     
        
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