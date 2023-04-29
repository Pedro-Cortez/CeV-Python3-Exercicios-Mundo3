from random import randint
from time import sleep
from operator import itemgetter

print('-=' * 20)
print('Disputa de Dados'.center(40, ' '))
print('-=' * 20)

cassino = dict()
ranking = list()
i = 1
cassino['Jogador1'] = randint(1, 6)
cassino['Jogador2'] = randint(1, 6)
cassino['Jogador3'] = randint(1, 6)
cassino['Jogador4'] = randint(1, 6)
print('Rodada de Lançamento de Dados:')
for k, v in cassino.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('-=' * 20)
print('===< RANKING DE JOGADORES >===')
ranking = sorted(cassino.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com o nº {v[1]}')
    sleep(1)
