from MySqlConnect import Connection, executeDatabaseCommand
from WsPartidas import getPartida
from WsTimes import getTimes
from WsCampeonato import getCampeonato

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

def verificarPartida(NumeroPartida):
    sql = "select id, numeroPartida from partidas";
    Connection.execute(sql);
    partidasCadastradasRaw = Connection.fetchall();
    
    for item in partidasCadastradasRaw:
        if(int(item[1]) == NumeroPartida):
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
            
def cadastrarPartidas(Campeonato, Divisao, Ano):
    jogo = 1
    jogoValido = True
    campeonato = verificarCampeonato(Campeonato, Divisao, Ano)
    existePartida = verificarPartida(jogo);
    
    if(campeonato[0] and not existePartida[0] and jogo<=380):
        while(jogoValido):
            partida = getPartida(Ano, jogo);

            mandante = verificarTime(partida.mandante_nome);
            visitante = verificarTime(partida.visitante_nome);
                
            if(mandante[0] and visitante[0]):
                sql = ("INSERT INTO partidas (numeroPartida, local, data, golsMandante, golsVisitante, cartoesAmarelosMandante, cartoesAmarelosVisitante, cartoesVermelhosMandante, cartoesVermelhosVisitante, campeonatoId, mandanteId, visitanteId, partidaRealizada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)");
                values = (partida.partida_numero, partida.partida_local, partida.partida_data, partida.mandante_placar, partida.visitante_placar, partida.mandante_cartoes_amarelos, partida.visitante_cartoes_amarelos, partida.mandante_cartoes_vermelhos, partida.visitante_cartoes_vermelhos, campeonato[1], mandante[1], visitante[1], partida.resultado_valido);
                    
                Connection.execute(sql, values)
                executeDatabaseCommand(); 
                print(jogo)
                jogo = jogo + 1
                    
            else:
                print("Mandante e/ou Visitante não localizado!")

    else:
        print("Campeonato não localizado!")
            
            
            
cadastrarPartidas('Campeonato Brasileiro de Futebol','Série A', 2023)  
#cadastrarTimes(2023)     
#cadastrarCampeonato(2023)
