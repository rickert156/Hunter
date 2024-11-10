from tools.bsHunter import parserLinks
from tools.responseEngine import responseEngine
from config import CounterRequest, TimeSleep
import time

def DuckSearch(pages, url):
    for pages in range(CounterRequest):
        response = responseEngine(url)
        print(f'Request [{pages+1}] :|: Status code: {response.status_code}')
        if response.status_code <= 300:parserLinks(response)
        else:print(f"Запрос отклонен")
        time.sleep(TimeSleep)



