from time import sleep

print('-=' * 20)
print('Maior Número da Sequência'.center(40, ' '))
print('-=' * 20)


def maior(* num):
    num_maior = 0
    for cont in range(0, len(num)):
        if cont == 0:
            num_maior = num[cont]
        elif num[cont] > num_maior:
            num_maior = num[cont]
    print(f'Analisando os valores informados...')
    print(f'Foram informados {len(num)} valor(es):', end=' ')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
    print()
    print(f'O maior valor informado foi {num_maior}.')
    print('-=' * 20)


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
