def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno que mede {larg}x{comp} é de {ar}m².')


print('--' * 20)
print('Controle de Área'.center(40, ' '))
print('--' * 20)
l = float(input(f'Largura (m): '))
c = float(input(f'Comprimento (m): '))
area(l, c)
