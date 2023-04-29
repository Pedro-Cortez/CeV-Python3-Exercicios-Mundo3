from time import sleep

print('-=' * 20)
print('CONTAGEM PERSONALIZADA'.center(40, ' '))
print('-=' * 20)


def contador(com, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {com} até {fim}, com passo {passo}:')
    sleep(1.5)
    if com < fim:
        cont = com
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont = cont + passo
            sleep(0.5)
        print('FIM!')
    else:
        cont = com
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont = cont - passo
            sleep(0.5)
        print('FIM!')


#Programa Principal
contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, 2)
print('-=' * 20)
print('Agora, personalize sua contagem!')
c = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
print('-=' * 20)
contador(c, f, p)
