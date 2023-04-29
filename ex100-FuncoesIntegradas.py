from random import randint
from time import sleep

print('-=' * 20)
print('Integrando Funções'.center(40, ' '))
print('-=' * 20)


def sorteia(valores):
    for cont in range(0, 5):
        valores.append(randint(1, 10))
    print(f'Sorteando 5 valores:', end=' ')
    for num in valores:
        print(f'{num}', end=' ')
        sleep(0.5)
    print('FEITO!')


def somaPar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos valores pares da lista {lst} é {soma}.')



#Programa principal
lista = list()
sorteia(lista)
somaPar(lista)
