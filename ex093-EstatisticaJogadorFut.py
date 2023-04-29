print('-=' * 30)
print('Aproveitamento de Jogador de Futebol'.center(60, ' '))
print('-=' * 30)

atleta = dict()
gol = list()
atleta['Nome'] = str(input('Nome do jogador: '))
jogos = int(input('Quantidade de partidas disputadas: '))
for cont in range(0, jogos):
    gol.append(int(input(f'Gols na partida {cont}: ')))
atleta['Gols'] = gol[:]
atleta['Saldo de Gols'] = sum(gol)
print('-=' * 30)
print(atleta)
print('-=' * 30)
for k, v in atleta.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {atleta["Nome"]} fez {jogos} partidas.')
for cont, g in enumerate(gol):
    print(f'    => Na partida {cont} marcou {g} gol(s)')
print(f'No total, marcou {atleta["Saldo de Gols"]} gols.')
