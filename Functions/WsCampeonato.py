import requests;
from bs4 import BeautifulSoup;

def getCampeonato(ano):
    url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{}'.format(str(ano));
    
    page = requests.get(url);
    soup = BeautifulSoup(page.text, 'html.parser');
    
    headers = soup.find_all('header');
    campeonato_raw = headers[1].h2.text;
    campeonato = campeonato_raw.split(' - ');
    
    return campeonato
