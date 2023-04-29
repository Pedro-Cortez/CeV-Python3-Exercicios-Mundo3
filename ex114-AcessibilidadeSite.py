from urllib import request

print('--' * 20)
print('VERIFICANDO ACESSIBILIDADE DE SITE'.center(40))
print('--' * 20)

try:
    site = request.urlopen('http://pudim.com.br')
except:
    print('\033[1;31m O site "pudim" não está acessível no momento!\033[m')
else:
    print('\033[1;32m O site "pudim" está acessível!\033[m')
