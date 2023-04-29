from time import sleep

c = ['\033[m', '\033[7;40m', '\033[41m', '\033[43m', '\033[44m']


def cabeca(cab, cor=0):
    print(c[cor], end='')
    print(f'~' * (len(cab) + 4))
    print(f'  {cab}')
    print(f'~' * (len(cab) + 4))
    print(c[0], end='')


def manual(com):
    cabeca(f'Acessando o manual do comando "{com}"', 4)
    print(c[1], end='')
    sleep(1)
    duvida = com
    help(com)
    print(c[0], end='')


while True:
    cabeca('SISTEMA DE AJUDA PYHELP', 3)
    duvida = str(input('Função ou Biblioteca > '))
    if duvida == 'fim':
        cabeca('Até Logo!', 2)
        break
    manual(duvida)
