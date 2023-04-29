print('-=' * 30)
print('DIVIDINDO VALORES EM VÁRIAS LISTAS'.center(60, ' '))
print('-=' * 30)

lista = list()
par = list()
impar = list()
while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    opcao = str(input('Continua? [S/N] '))
    while opcao not in 'SNsn':
        opcao = str(input('Continua? [S/N]'))
    if opcao in 'Nn':
        break
for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-=' * 30)
print(f'Lista completa: {lista}.')
print(f'Lista de valores pares: {par}')
print(f'Lista de valores ímpares: {impar}')
