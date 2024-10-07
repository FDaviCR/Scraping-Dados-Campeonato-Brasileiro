import requests
from bs4 import BeautifulSoup

def getTimes(ano):
    url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{}'.format(str(ano))
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    spans = soup.find_all('span')
    
    tgt_class_time = 'hidden-xs'
    
    times = []
    for span in spans:
        if(span.get('class') != None):
            if tgt_class_time in span.get('class'):
                times.append(span.text)

    return times