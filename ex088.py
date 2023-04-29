from random import randrange
from time import sleep

print('-=' * 20)
print('PALPITES ALEATÓRIOS: MEGA SENA'.center(40, ' '))
print('-=' * 20)

palpite = list()
jogo = list()

quant = int(input('Quantos jogos deseja sortear? '))
for jog in range(0, quant):
    for num in range(0, 6):
        jogo.append(randrange(1, 60))
    palpite.append(jogo[:])
    jogo.clear()
print('-=' * 5, f' Sorteando {quant} jogos ', '-=' * 5)
for pos, sorteio in enumerate(palpite, start=1):
    sorteio.sort()
    sleep(1)
    print(f'Jogo {pos}: {sorteio}')
print('-=' * 8, f'Boa Sorte', '-=' * 7)
