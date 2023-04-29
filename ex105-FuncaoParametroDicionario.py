print('-=' * 20)
print('FUNÇÃO: DICIONÁRIO COM NOTAS'.center(40, ' '))
print('-=' * 20)


def notas(*provas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param provas: aceita quantidade flexível de notas.
    :param sit: valor opcional, indica se a situação da turma será incluída.
    :return: dicionário com o desempenho da turma.
    """
    desemp = dict()
    soma = 0
    desemp['Total'] = len(provas)
    for cont in range(0, len(provas)):
        if cont == 0:
            maior = menor = provas[0]
        else:
            if provas[cont] > maior:
                maior = provas[cont]
            if provas[cont] < menor:
                menor = provas[cont]
        soma = soma + provas[cont]
    media = soma / len(provas)
    desemp['Maior'] = maior
    desemp['Menor'] = menor
    desemp['Média'] = media
    if sit == True:
        if media >= 7:
            desemp['Situação'] = 'Boa'
        elif 5 <= media < 7:
            desemp['Situação'] = 'Razoável'
        elif media < 5:
            desemp['Situação'] = 'Ruim'
    return desemp


#Programa principal
resp = notas(10, 5.5, 2.5, 9, 8.5, sit=True)
help(notas)
print(resp)
