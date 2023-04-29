from random import randint
print(' SORTEANDO DE NÚMEROS '.center(60, '#'))
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')
