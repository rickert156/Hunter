from tools.menu import menu
from tools.editConfig import EditConfig
from tools.mainTools import readSetLinks
from tools.searchEngine import DuckDuckGo
from tools.duck import DuckSearch
from tools.proxy import proxyRequest

def startSearch(number):
    requestEngine = False
    
    if number == 10:return EditConfig()
    if number == 1:requestEngine = DuckDuckGo
    else:requestEngine = DuckDuckGo
    
    user_request = input("Запрос: ")

    print(f'Отладка: поисковик - {requestEngine}')
    url = f'{requestEngine}{user_request}'
    proxyRequest()
    pages = 0
    if requestEngine != False:DuckSearch(pages, url)

    readSetLinks()

def userRequest():
    try:
        menu()
        try:searchEngine = int(input("Способ Поиска информации: "))
        except:print('Некорректный выбор!')
        startSearch(searchEngine)
    except KeyboardInterrupt:print('\nВыход из программы\n')

userRequest()
