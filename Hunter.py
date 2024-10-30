from tools.menu import menu
from tools.mainTools import readSetLinks
from tools.searchEngine import DuckDuckGo, Metabot
from tools.duck import DuckSearch

def startSearch(user_request, number):
    searchEngine = False
    if number == 1:searchEngine = DuckDuckGo
    if number == 2:searchEngine = Metabot
    else:searchEngine = DuckDuckGo

    print(f'Отладка: поисковик - {searchEngine}')
    url = f'{searchEngine}{user_request}'
    pages = 0
    DuckSearch(pages, url)

    readSetLinks()

def userRequest():
    try:
        menu()
        try:searchEngine = int(input("Какой поисковой системой будем пользоваться: "))
        except:print('Некорректный выбор!')
        user_request = input("Запрос: ")
        startSearch(user_request, searchEngine)
    except KeyboardInterrupt:print('\nВыход из программы\n')

userRequest()
