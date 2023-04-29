print('-=' * 30)
print('Estaísticas de Time de Futebol'.center(60, ' '))
print('-=' * 30)

jgdor = dict()
gol = list()
time = list()
while True:
    jgdor.clear()
    jgdor['Nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Partidas disputadas por {jgdor["Nome"]}: '))
    for cont in range(0, jogos):
        gol.append(int(input(f'Gols na partida {cont + 1}: ')))
    jgdor['Gols'] = gol[:]
    jgdor['Saldo'] = sum(gol)
    time.append(jgdor.copy())
    gol.clear()
    opcao = str(input('Gostaria de Continuar? [S/N] ')).upper()[0]
    while opcao not in 'SN':
        print('ERRO! Digite um opção válida.')
        opcao = str(input('Gostaria de continuar? [S/N]')).upper()[0]
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Cód ', end='')
for i in jgdor.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)
while True:
    busca = int(input('Qual desempenho individual gostaria de ver? [999 para sair] '))
    if busca == 999:
        print()
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f'-- ESTATÍSTICA DO JOGADOR {time[busca]["Nome"]}:')
        for part, g in enumerate(time[busca]["Gols"]):
            print(f'   Na partida {part + 1} marcou {g} gols.')
    print('--' * 30)
print('<<< FIM DO PROGRAMA >>>')
