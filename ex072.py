print(' NÚMERO POR EXTENSO '.center(60, '-'))

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha not in range(0, 21):
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num[escolha]}.')
    opcao = str(input('Você gostaria de continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(' Fim do exercício '.center(60, '-'))
