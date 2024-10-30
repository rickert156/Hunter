from bs4 import BeautifulSoup
from tools.menu import menu
from tools.links import RESULT_LINK
from tools.mainTools import readSetLinks
from tools.searchEngine import DuckDuckGo
from config import CounterRequest, UserAgent, TimeSleep
import requests, time

def InitBS(response):
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

def startSearch(user_request, number):
    if number == 1:searchEngine = DuckDuckGo
    else:searchEngine = DuckDuckGo
    def count(page, status):
        print(f'Request [{page}] :|: Status code: {status}')

    headers = {'User-Agent':UserAgent}

    url = f'{searchEngine}{user_request}'
    pages = 0
    print(f'Отладка: поисковик - {searchEngine}')
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
        time.sleep(TimeSleep)
        if pages == CounterRequest:
            break

    readSetLinks()

def userRequest():
    try:
        menu()
        try:
            searchEngine = int(input("Какой поисковой системой будем пользоваться: "))
        except:print('Некорректный выбор!')
        user_request = input("Запрос: ")
        startSearch(user_request, searchEngine)
    except KeyboardInterrupt:print('\nВыход из программы\n')

userRequest()
