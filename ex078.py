print('=-' * 30)
print('LISTA: MAIOR E MENOR VALOR'.center(60, ' '))
print('=-' * 30)

alg = list()
for cont in range(0, 5):
    alg.append(int(input(f'Digite um valor para posição {cont}: ')))

print('=-' * 30)
print(f'Você digitou os algarismos {alg}.')
print(f'O maior valor é {max(alg)} e está na posicão:', end=' ')
for pos, num in enumerate(alg):
    if num == max(alg):
        print(f'{pos}...', end=' ')
print()
print(f'O menor valor é {min(alg)} e está na posição:', end=' ')
for pos, num in enumerate(alg):
    if num == min(alg):
        print(f'{pos}...', end=' ')
print()
