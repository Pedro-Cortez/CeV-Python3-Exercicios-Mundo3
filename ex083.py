print('-=' * 30)
print('VALIDANDO EXPRESSÕES MATEMÁTICAS'.center(60, ' '))
print('-=' * 30)

express = str(input('Digite uma expressão matemática para validação: '))
parentese_a = express.count('(')
parenteset_f = express.count(')')
prt = parentese_a + parenteset_f
if prt % 2 == 0:
    print('Expressão matemática válida!')
else:
    print('Expressão matemática inválida!')
