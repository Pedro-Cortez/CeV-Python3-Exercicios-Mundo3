print('**' * 20)
print('MANIPULANDO MATRIZES'.center(40, ' '))
print('**' * 20)

maior2 = s3 = SomaPar = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha}, {coluna}] da matriz: '))
print('**' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            SomaPar = SomaPar + matriz[linha][coluna]
    print()
print('**' * 20)
for cont in range(0, 3):
    if matriz[1][cont] > maior2:
        maior2 = matriz[1][cont]
    s3 = s3 + matriz[cont][2]
print(f'A soma dos valores da terceira coluna é {s3}.')
print(f'O maior valor da segunda linha é {maior2}.')
print(f'A soma dos valores pares é igual a {SomaPar}.')
