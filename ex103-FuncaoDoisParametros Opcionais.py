print('-+' * 20)
print('Contagem de Gols'.center(40, ' '))
print('-+' * 20)


def ficha(jog='<desconhecido>', g=0):
    print(f'O jogador {jog} fez {g} gol(s) no campeonato.')


#Programa principal
jogador = str(input('Nome do atleta: '))
gol = str(input('Total de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(g=gol)
else:
    ficha(jogador, gol)

