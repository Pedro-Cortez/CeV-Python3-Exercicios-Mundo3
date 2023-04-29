print('**' * 30)
print('LISTA COMPOSTA PARES E ÍMPARES'.center(60, ' '))
print('**' * 30)

conjunto = [[], []]
for cont in range(1, 8):
    num = (int(input(f'Digite o {cont}º valor: ')))
    if num % 2 == 0:
        conjunto[0].append(num)
    else:
        conjunto[1].append(num)
print('-=' * 30)
conjunto[0].sort()
conjunto[1].sort()
print(f'Os valores pares digitados foram {conjunto[0]}.')
print(f'Os valores ímpares digitads foram {conjunto[1]}.')
