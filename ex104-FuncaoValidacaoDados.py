print('-=' * 20)
print('VALIDAÇÃO DE DADOS'.center(40))
print('-=' * 20)


def leiaInt(mens):
    valor = 0
    while True:
        n = str(input(mens))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print(f'\033[1;31mErro! Digite um número inteiro válido.\033[m')


#Programa principal
n = leiaInt('Digite um número: ')
print(f'\033[0;32mVocê digitou o número {n}.\033[m')
