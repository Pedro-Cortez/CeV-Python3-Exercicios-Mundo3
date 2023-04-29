print(' Analisando tupla numérica '.center(60, '+'))
print('Digite quatro números abaixo')
num_a = int(input('1º valor: '))
num_b = int(input('2º valor: '))
num_c = int(input('3º valor: '))
num_d = int(input('4º valor: '))
tupla = (num_a, num_b, num_c, num_d)
print(f'O número 9 apareceu {tupla.count(9)} vez(es).')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Foram digitados os seguintes números pares: ', end='')
for par in tupla:
    if par % 2 == 0:
        print(par, end=' ')
