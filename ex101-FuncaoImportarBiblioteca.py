print('-=' * 20)
print('ANÁLISE DE IDADE ELEITORAL'.center(40, ' '))
print('-=' * 20)


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print('--' * 20)
    if idade < 16:
        return f'{idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 70:
        return f'{idade} anos: VOTO OPCIONAL. '
    else:
        return f'{idade} anos: VOTO OBRIGATÓRIO.'


#Programa principal
nasc = int(input('Informe o ano de nascimento: '))
print(voto(nasc))
