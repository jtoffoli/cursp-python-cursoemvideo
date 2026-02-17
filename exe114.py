import requests

try:
    requests.get(url='http://www.pudim.com.br')
    print('Site acessível')
except:
    print('Site inacessível')