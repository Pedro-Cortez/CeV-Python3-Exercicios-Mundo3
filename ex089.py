from time import sleep

print('-=' * 20)
print('BOLETIM COM LISTAS COMPOSTAS'.center(40, ' '))
print('-=' * 20)

dados = list()
boletim = list()

while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    opcao = str(input('Continua? [S/N] '))
    while opcao not in 'SsNn':
        opcao = str(input('Continua? [S/N] '))
    if opcao == 'N' or opcao == 'n':
        break
print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA"}')
print('-' * 20)
for pos, cont in enumerate(dados):
    print(f'{pos:<3} {cont[0]:<10} {cont[2]:.1f}')
while True:
    print('-=' * 30)
    aluno = int(input('Qual desempenho individual gostaria de mostra (999 para encerrar): '))
    if 0 <= aluno < len(dados):
        print(f'As notas de {dados[aluno][0]} são {dados[aluno][1]}')
    if aluno == 999:
        print('Finalizando...')
        sleep(1)
        print(f'{"<<<   FIM DO PROGRAMA  >>>"}')
        break