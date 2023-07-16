from Database.MySqlConnect import Connection, executeDatabaseCommand
from Scraping.WsPartidas import getPartida
from Scraping.WsTimes import getTimes
from Scraping.WsCampeonato import getCampeonato

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

def verificarPartida(NumeroPartida, Campeonato):
    sql = ("select id, numeroPartida, partidaRealizada from partidas where numeroPartida = %s and campeonatoId = %s");
    values = (NumeroPartida, Campeonato,)
    Connection.execute(sql, values)
    
    partida = Connection.fetchall();
    if (len(partida) == 1):
        return [True, partida[0][0], partida[0][1], partida[0][2]]
    else:
        return [False, 0, 0, 0]

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
    campeonato = verificarCampeonato(Campeonato, Divisao, Ano)
    
    
    if(campeonato[0]):
        while(jogo<=380):
            existePartida = verificarPartida(jogo, campeonato[1]);
            
            if(not existePartida[0]):
                partida = getPartida(Ano, jogo);

                mandante = verificarTime(partida.mandante_nome);
                visitante = verificarTime(partida.visitante_nome);
                
                if(int(partida.partida_numero) % 10 == 0):
                    rodada = int(partida.partida_numero)/10
                else:
                    rodada = (int(partida.partida_numero) + 10) // 10
                      
                if(mandante[0] and visitante[0]):
                    sql = ("INSERT INTO partidas (numeroPartida, local, data, golsMandante, golsVisitante, cartoesAmarelosMandante, cartoesAmarelosVisitante, cartoesVermelhosMandante, cartoesVermelhosVisitante, campeonatoId, mandanteId, visitanteId, partidaRealizada, rodada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)");
                    values = (partida.partida_numero, partida.partida_local, partida.partida_data, partida.mandante_placar, partida.visitante_placar, partida.mandante_cartoes_amarelos, partida.visitante_cartoes_amarelos, partida.mandante_cartoes_vermelhos, partida.visitante_cartoes_vermelhos, campeonato[1], mandante[1], visitante[1], partida.resultado_valido, rodada);
                            
                    Connection.execute(sql, values)
                    executeDatabaseCommand(); 
                    jogo = jogo + 1
                            
                else:
                    print("Mandante e/ou Visitante não localizado!")
            else:
                sql = ("select id, partidaRealizada from partidas where campeonatoId = %s and numeroPartida = %s")
                values = (campeonato[1],jogo,)
                Connection.execute(sql, values)
                print("Jogo: " + str(jogo))
                
                partidaRealizada = Connection.fetchall();    
                partida = getPartida(Ano, jogo);
                
                if(partidaRealizada == []):
                    partidaRealizada = [(0, 1)]

                mandante = verificarTime(partida.mandante_nome);
                visitante = verificarTime(partida.visitante_nome);  
                
                if(int(partida.partida_numero) % 10 == 0):
                    rodada = int(partida.partida_numero)/10
                else:
                    rodada = (int(partida.partida_numero) + 10) // 10
                           
                if(mandante[0] and visitante[0]):
                    sql = ("UPDATE partidas SET local = %s, data = %s, golsMandante = %s, golsVisitante = %s, cartoesAmarelosMandante = %s, cartoesAmarelosVisitante = %s, cartoesVermelhosMandante = %s, cartoesVermelhosVisitante = %s, partidaRealizada = %s, rodada = %s WHERE id = %s");
                    values = (partida.partida_local, partida.partida_data, partida.mandante_placar, partida.visitante_placar, partida.mandante_cartoes_amarelos, partida.visitante_cartoes_amarelos, partida.mandante_cartoes_vermelhos, partida.visitante_cartoes_vermelhos, partida.resultado_valido, rodada, partidaRealizada[0][0]);
                            
                    Connection.execute(sql, values)
                    executeDatabaseCommand(); 
                    jogo = jogo + 1
                            
                else:
                    print("Mandante e/ou Visitante não localizado!")
                
    else:
        print("Campeonato não localizado!")
            

cadastrarCampeonato(2020)  
cadastrarTimes(2020)       
cadastrarPartidas('Campeonato Brasileiro de Futebol','Série A', 2020)  

