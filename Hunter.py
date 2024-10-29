from bs4 import BeautifulSoup
from tools.links import RESULT_LINK
from tools.mainTools import readSetLinks
from config import CounterRequest, UserAgent
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
    #readSetLinks()

def startDuck(user_request):
    
    def count(page, status):
        print(f'Request [{page}] :|: Status code: {status}')

    headers = {'User-Agent':UserAgent}

    url = f'https://html.duckduckgo.com/html/?q=/{user_request}'
    pages = 0
    for pages in range(CounterRequest):
        response = requests.get(url, headers=headers)
        resp_status = response.status_code
        if resp_status <= 300:
            pages+=1
            count(pages, resp_status)
            InitBS(response)
        else:
            pages+=1
            print(f"Запрос отклонен")
            count(pages, resp_status)
            #startDuck(user_request)
        if pages == CounterRequest:
            break

    readSetLinks()

def userRequest():
    user_request = input("Запрос: ")
    startDuck(user_request)

userRequest()
