print('-=' * 20)
print('CALCULANDO FATORIAL'.center(40, ' '))
print('-=' * 20)


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número a ser calculado.
    :param show: Opcional para demonstração de cálculo.
    :return: Resultado do fatorial
    """
    fat = 1
    for cont in range(num, 0, -1):
        fat = fat * cont
        if show:
            print(f'{cont}!', end=' ')
    return f'= {fat}'


#Programa principal
print(fatorial(5, True))
#help(fatorial)
