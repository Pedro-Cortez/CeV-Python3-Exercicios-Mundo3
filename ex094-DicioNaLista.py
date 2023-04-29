print('-=' * 20)
print('Cadastro Geral de Pessoas'.center(40, ' '))
print('-=' * 20)

dados = dict()
cadastro = list()
somaId = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while dados['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas "M" ou "F".')
        dados['Sexo'] = str(input('Sexo: [M/F] '))
    dados['Idade'] = int(input('Idade: '))
    cadastro.append(dados.copy())
    opcao = str(input('Gostaria de continuar o cadastro? [S/N] ')).upper()[0]
    while opcao not in 'SN':
        print('ERRO! Digite apenas "S" ou "N".')
        opcao = str(input('Gostaria de continuar o cadastro? [S/N] '))
    if opcao in 'N':
        break
print('-=' * 30)
for cont in range(0, len(cadastro)):
    somaId = somaId + cadastro[cont]['Idade']
    medId = somaId / len(cadastro)
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
print(f'B) Média de idade é de {medId:5.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in cadastro:
    if p['Sexo'] in 'F':
        print(p['Nome'], end=' ')
print()
print('D) Lista de pessoas acima da média de idade:')
for p in cadastro:
    if p['Idade'] >= medId:
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
        print()
print('<<< Fim do Programa >>>')
