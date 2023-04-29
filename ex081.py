print('-=' * 30)
print('EXTRAINDO DADOS DE UMA LISTA'.center(60, ' '))
print('-=' * 30)

lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opcao = str(input('Continua? [S/N] ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('Continua? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente são: {lista}.')
if 5 in lista:
    print('O número 5 foi incluído na lista.')
else:
    print('O número 5 não foi incluído na lista.')
