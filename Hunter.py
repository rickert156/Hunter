from tools.menu import menu
from tools.editConfig import EditConfig
from tools.mainTools import readSetLinks
from tools.searchEngine import DuckDuckGo, Metabot
from tools.duck import DuckSearch

def startSearch( number):
    searchEngine = False
    
    if number == 10:return EditConfig()
    if number == 1:searchEngine = DuckDuckGo
    if number == 2:searchEngine = Metabot
    else:searchEngine = DuckDuckGo
    
    user_request = input("Запрос: ")

    print(f'Отладка: поисковик - {searchEngine}')
    url = f'{searchEngine}{user_request}'
    pages = 0
    if searchEngine == DuckDuckGo:DuckSearch(pages, url)

    readSetLinks()

def userRequest():
    try:
        menu()
        try:searchEngine = int(input("Какой поисковой системой будем пользоваться: "))
        except:print('Некорректный выбор!')
        startSearch(searchEngine)
    except KeyboardInterrupt:print('\nВыход из программы\n')

userRequest()
