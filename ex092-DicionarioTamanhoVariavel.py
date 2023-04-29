from datetime import date

print('-=' * 20)
print('Cadastro de Tabalhador'.center(40, ' '))
print('-=' * 20)

empresa = dict()
empresa['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
empresa['Idade'] = hoje - ano_nasc
ctps = int(input('Carteira de Trabalho (0 para "Não Possui"): '))
if ctps == 0:
    empresa['Carteira de Trabalho'] = 'Não Possui'
    print('-=' * 20)
    for k, v in empresa.items():
        print(f'{k} do colaborador: {v} ')
else:
    empresa['Carteira de Trabalho'] = ctps
    empresa['Contratação'] = int(input('Ano de contratação: '))
    empresa['Salário'] = float(input('Salário: R$ '))
    empresa['Aposentadoria'] = (empresa['Contratação'] + 35) - ano_nasc
    print('-=' * 20)
    for k, v in empresa.items():
        print(f'{k} do colaborador: {v}')
