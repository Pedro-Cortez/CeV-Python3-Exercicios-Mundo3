print('-' * 45)
print('TABELA DE PREÇOS'.center(45, ' '))
print('-' * 45)
estoque = ('Notebook', 4500.00, 'Mouse', 75.00, 'Teclado', 200.00, 'Headphone', 150.00, 'SSD', 400.00,
           'HD Externo', 230.00, 'Mousepad', 20.00, 'Cabo HDMI', 15.00)
for pos, produto in enumerate(estoque):
    if pos % 2 == 0:
        print(f'{produto:.<34}', end=' ')
    if pos % 2 != 0:
        print(f'R$ {produto:7.2f}')
print('-' * 45)
