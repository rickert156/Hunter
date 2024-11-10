import requests, time, random
from config import UserAgent
from tools.proxie_list import PROXIE_LIST
from tools.menu import GREEN, RESET
def randProxie():
    global PROXIE_LIST
    selectProxie = random.choice(PROXIE_LIST)
    return selectProxie


def responseEngine(url):
    proxy = randProxie()
    print(f'{GREEN}Select Proxy: {proxy}{RESET}')
    headers = {'User-Agent':UserAgent}
    response = requests.get(url, headers=headers, proxies={'http':proxy})
    
    return response

