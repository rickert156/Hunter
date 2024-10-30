import os, shutil

CONFIG = 'config.py'
TEMP = 'temp.py'

line = '*'*20

def readFile():
    global CONFIG
    with open(CONFIG, 'r') as file:
        for config in file.readlines():
            config = config.strip()
            print(config)

def EditConfig():
    global CONFIG 
    readFile()
    
    print(line)

    CounterRequest = input("Новое значение CounterRequest: ")
    TimeSleep = input("Новое значениче TimeSleep: ")
    UserAgent = input("Новое значение UserAgent: ")
    
    print(line)
    
    try:CounterRequest = int(CounterRequest)
    except:CounterRequest = 10
    try:TimeSleep = int(TimeSleep)
    except:TimeSleep = 0
    if len(UserAgent) <= 1:UserAgent = "GoogleBot"
    
    with open(TEMP, 'w') as rewrite:
        write = rewrite.write(f'CounterRequest = {CounterRequest}\nTimeSleep = {TimeSleep}\nUserAgent = "{UserAgent}"\n')
    
    os.remove(CONFIG)
    shutil.move(TEMP, CONFIG)

    readFile()
