print('=' * 50)
print('CONTADOR DE VOGAIS'.center(50, ' '))
print('=' * 50)

palavras = ('servidor', 'direito', 'doutrina', 'julgado', 'tribunal',
            'jurista', 'advogado', 'procurador', 'promotor', 'lei')

for texto in palavras:
    print(f'\nNa palavra \033[1;31m{texto}\033[m temos as vogais: ', end=' ')
    for vogal in texto:
        if vogal in 'aeiou':
            print(vogal, end=' ')

