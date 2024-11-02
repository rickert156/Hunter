from tools.searchEngine import DuckDuckGo

START_URL = DuckDuckGo

def DorkSite():
    url = START_URL
    dork = "site:"
    request = f'{url}{dork}'

    return request

    
