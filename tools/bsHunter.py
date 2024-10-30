from bs4 import BeautifulSoup
from tools.links import RESULT_LINK

def parserLinks(response):
    response = response.text
    bs = BeautifulSoup(response, 'lxml')
    #print(bs.body)
    for links in bs.find_all('a'):
        try:
            link = links.attrs['href']
            if 'duckduckgo.com/feedback.html' not in link:
                link = link.split('=')[1]
                RESULT_LINK.add(f'{link}')
        except:pass
