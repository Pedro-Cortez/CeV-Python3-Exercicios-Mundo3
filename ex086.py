print('**' * 20)
print('CRIANDO MATRIZES'.center(40, ' '))
print('**' * 20)

matriz = [[], [], []]
for cont in range(0, 3):
    matriz[0].append(int(input(f'Digite o valor [0, {cont}] da Matriz: ')))
for cont in range(0, 3):
    matriz[1].append(int(input(f'Digite o valor [1, {cont}] da Matriz: ')))
for cont in range(0, 3):
    matriz[2].append(int(input(f'Digite o valor [2, {cont}] da Matriz: ')))
print('**' * 30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
