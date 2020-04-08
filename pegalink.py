# small script to get dates on this: https://baiak-ilusion.com/?subtopic=highscores
import requests
from time import sleep
from bs4 import BeautifulSoup as b4


banco = []  # save values of the queries

def path():
    base_url = 'https://baiak-ilusion.com/'
    for i in range(50):
        yield f'{base_url}?subtopic=highscores&list=experience&page={i}&vocation=&world=0'

   
take_link = path()


while True:
    try:
        search = requests.get(next(take_link))  # acess page
        sleep(1)
    except:
        print('final')
        break
    # craling pages
    create_obj = b4(search.text, 'html.parser')  # convert in obj bs4
    tabela_rank = create_obj.find('table', {'class': 'TableContent'}).find_all('tr')  # take table of rank
    for i in range(2, 102):
        persons: str = tabela_rank[i].find_all('td')
        names: str = persons[1].find('a').text
        vocation: str = persons[1].find('p').text
        level: int = persons[2].text
        exp: int = persons[3].text
        banco.append({'nome': names, 'classe': vocation.strip('[]'), 'level': int(level), 'exp': int(exp)})
    print(f'Os dados de {names} foram capturados')


with open('dados.txt', 'w') as f:
    for row in banco:
        f.write(f'{row}\n')
