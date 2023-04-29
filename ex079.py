cor = {'vermelho': '\033[31m',
        'limpa': '\033[m'}

print(f'{cor["vermelho"]}')
print('*' * 60)
print('CADASTRO DE VALORES ÚNICOS'.center(60, ' '))
print('*' * 60)
print(f'{cor["limpa"]}', end='')
valor = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valor:
        valor.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Número não adicionado.')
    opcao = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print(f'{cor["vermelho"]}', end='')
print('*' * 60, end='')
print(f'{cor["limpa"]}')
valor.sort()
print(f'Você digitou os valores {valor}')
