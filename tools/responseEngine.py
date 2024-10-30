import requests
from config import UserAgent

def responseEngine(url):
    headers = {'User-Agent':UserAgent}
    response = requests.get(url, headers=headers)
    
    return response

