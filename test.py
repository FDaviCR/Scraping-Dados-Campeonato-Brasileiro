from Mysql_connect import Connection
from Ws_partidas import getJogos

#Connection.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

test = getJogos(2023, 3);

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
