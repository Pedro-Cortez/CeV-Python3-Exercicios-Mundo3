print('-=' * 20)
print('Dicionário: Arquivo de Médias Escolares'.center(40, ' '))
print('-=' * 20)

escola = dict()
escola['Aluno'] = str(input('Nome do Aluno: '))
escola['Media'] = float(input(f'Média de {escola["Aluno"]}: '))
if escola["Media"] >= 7:
    escola["Situação"] = 'Aprovado'
elif 5 <= escola["Media"] < 7:
    escola["Situação"] = 'Recuperação'
elif escola["Media"] < 5:
    escola["Situação"] = 'Reprovado'
print('-=' * 20)
for k, v in escola.items():
    print(f'- {k} é igual a {v}')
