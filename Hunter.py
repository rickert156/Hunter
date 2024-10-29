from bs4 import BeautifulSoup
from tools.links import RESULT_LINK
from tools.mainTools import readSetLinks
import requests

def InitBS(response):
    global RESULT_LINK
    response = response.text
    bs = BeautifulSoup(response, 'lxml')
    #print(bs.body.get_text())
    for links in bs.find_all('a'):
        try:
            link = links.attrs['href']
            if 'duckduckgo.com/feedback.html' not in link:
                link = link.split('=')[1]
                RESULT_LINK.add(f'{link}')
        except:pass
    readSetLinks()

def startDuck(user_request):
    
    headers = {'User-Agent':'GoogleBot'}

    url = f'https://html.duckduckgo.com/html/?q=/{user_request}'
    response = requests.get(url, headers=headers)
    resp_status = response.status_code
    if resp_status == 200:
        print(f'Status code: {resp_status}\n')
        InitBS(response)
    else:
        print(f"Запрос отклонен")
        startDuck(user_request)
        print(f'Status code: {resp_status}\n')

def userRequest():
    user_request = input("Запрос: ")
    startDuck(user_request)

userRequest()
