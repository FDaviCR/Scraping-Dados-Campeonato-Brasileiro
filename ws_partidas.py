import requests;
import re;
import datetime;
from datetime import date;
from bs4 import BeautifulSoup;

meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];

def getJogos(ano, partida):
    url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/'+str(ano)+'/'+str(partida)+'#escalacao';
    
    page = requests.get(url);
    soup = BeautifulSoup(page.text, 'html.parser');
    
    divs = soup.find_all('div');
    spans = soup.find_all('span')
    tgt_class_left = 'time-left';
    tgt_class_right = 'time-right';

    class Partida:
        resultado_valido = False
        msg = ''
        partida_local = ''
        partida_data = ''
        partida_horario = ''
        partida_numero = 0
        mandante_nome = ''
        mandante_placar = 0
        visitante_nome = ''
        visitante_placar = 0

    partida = Partida();
        
    partida.partida_numero = re.sub('[^0-9]', '', divs[7].span.text)
    hoje = datetime.date.today()
    
    data = re.sub('[^0-9]', '', spans[4].text)
    data_mes = str(meses.index(spans[4].text.split('de ')[1].replace(' ','').lower()) + 1);
    data_dia = data[0:2];
    data_ano = data[2:7];
    data_jogo = date(int(data_ano), int(data_mes), int(data_dia))
    partida.partida_horario = spans[5].text
    partida.partida_data = data_jogo;
    rawLocal = spans[3].text.replace('\r', '').replace('\n', '').split(' - ')
    partida.partida_local = rawLocal[0].replace(' ', '')+', '+rawLocal[1]+', '+rawLocal[2].replace(' ', '')
    
    if(data_jogo < hoje):
        for div in divs:
            if(div.get('class') != None):
                if tgt_class_left in div.get('class'):
                    partida.mandante_nome = div.h3.text;
                    partida.mandante_placar = int(div.strong.text);
                if tgt_class_right in div.get('class'):
                    partida.visitante_nome = div.h3.text;
                    partida.visitante_placar = div.strong.text;
                partida.msg = 'Dados capturados com sucesso!';
                partida.resultado_valido = True
    else:
        partida.resultado_valido = False
        partida.msg = 'Partida ainda não realizada!'
                    
    return partida;

'''
test = getJogos(2023, 1);

if(hasattr(test, 'mandante_placar')):
    print(test.partida_numero);
    print(test.mandante_nome);
    print(test.mandante_placar);
    print(test.visitante_nome);
    print(test.visitante_placar);  
    print(test.partida_local);
    print(test.partida_data)
'''