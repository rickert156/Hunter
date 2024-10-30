<div align="center">
  <img src="https://github.com/rickert156/rickert156/blob/main/assets/Hunter2.png" alt="Hunter">
</div>

# Hunter
## Поиск информации через различные поисковые системы
На данный момент поиск идет только через DuckDuckGo. Некоторые параметры можно регулировать через файл конфигурации config.py. <p>
В нем можно менять количество запросов:
```sh
# Будет 20 запросов
CounterRequest = 20 
```
Установка задержки запросов - Time Sleep
```sh
# Задерка будет 3 секунды
TimeSleep = 3
```
Можно поменять User-Agent. 
```sh
# Выдаем себя за гугл бота
UserAgent = 'GoogleBot'
```
Если нужны генераторы User-Agent, можно воспользоваться мини-библиотекой из другого репозитория - <a href="https://github.com/rickert156/Millennion">Millennion</a>
