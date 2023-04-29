print('-=' * 30)
print('LISTA COMPOSTA E ANÁLISE DE DADOS'.center(60, ' '))
print('-=' * 30)

info = list()
cad = list()
maior = menor = 0
while True:
    info.append(str(input('Nome: ')))
    info.append(float(input('Peso (kg): ')))
    if len(cad) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]
    cad.append(info[:])
    info.clear()
    opcao = str(input('Continua? [S/N] '))
    while opcao not in 'SsNn':
        opcao = str(input('Continua? [S/N]'))
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cad)} pessoas.')
print(f'O maior peso foi de {maior} Kg e pertence à ', end='')
for pessoa in cad:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor} Kg e pertence à ', end='')
for pessoa in cad:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print()
