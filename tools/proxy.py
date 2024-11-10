import requests, json
from bs4 import BeautifulSoup
from tools.proxie_list import PROXIE_LIST

def parserJson(response):
    global PROXIE_LIST
    print('Collecting proxy...')
    parser = response.json()
    number = 0
    for pars in parser:
        address = pars['address']
        protocols = pars['protocols'][0]
        country = pars['country']
        ping = pars['ping']
        anonymityLevel = pars['anonymityLevel']
        if protocols == 'http' or protocols == 'https':
            number+=1
            #print(f'[{number}] {protocols}\t{address}\tping {ping}\t{country}\tanonymityLevel: {anonymityLevel}')
            proxie = f'{protocols}://{address}'
            PROXIE_LIST+=[proxie]

    print(f'Number of Proxy: {len(PROXIE_LIST)}')
    
def proxyRequest():
    headers = {
        'Authorization': 'BgPXfhUc8CAhK7wGOqzqz9m77j3sH7',
        'Content-Type': 'application/json'
            }
    site = 'https://geoxy.io/proxies?count=9999'
    response = requests.get(site, headers=headers)
    resp = response.status_code
    parserJson(response)

