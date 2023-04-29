print('--' * 20)
print('VALIDAÇÃO COM TRATAMENTO DE EXCEÇÃO'.center(40))
print('--' * 20)


def leiaInt(mens):
    while True:
        try:
            valor = int(input(mens))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;35mO usuário não digitou valor inteiro! \033[m')
            return 0
        else:
            return valor


def leiaFloat(txt):
    while True:
        try:
            valor = float(input(txt))
        except(ValueError, TypeError):
            print(f'\033[1;31mErro! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;35mO usuário não digitou valor real! \033[m')
            return 0
        else:
            return valor



#Programa principal
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'\033[1;33mVocê digitou o número inteiro {i} e o número real {r}.\033[m')
