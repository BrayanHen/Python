import urllib.request

try:
    site=urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print(f'\033[31mO site pudim não está acessivel no momento!\033[m')
else:
    print(f'\033[32mO site pudim está acessivel!\033[m')