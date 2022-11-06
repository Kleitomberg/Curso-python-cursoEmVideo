#DESAFIO 105

def maior(lista):
    maior = 0
    for i, n in enumerate(lista):
        if i == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    return maior
def menor(lista):
    menor = 0
    for i, n in enumerate(lista):
        if i == 0:
            menor = n
        else:
            if n < menor:
                menor = n
    return menor
def media(lista):
    media = soma = 0
    soma = sum(lista)
    media = soma/len(lista)
    return media
def situacao(media):
    if media >=7:
        return "BOA"
    elif media >=6:
        return "RAZOÁVEL"
    else:
        return "RUIM"

def notas(*notas,sit=False):
    """

    :param notas: RECEBE N NOTAS dos alunos de uma turma
    :param sit: OPCIONAL - DEFINE SE SERÁ ADICIONADO A SITUAÇÃO DA TURMA AO DICIONARIO
    :return: Um dicionario com as informações da turma
    """
    boletim = dict()
    boletim['TOTnotas'] = len(notas)
    boletim['maiorNota'] = maior(notas)
    boletim['menorNota'] = menor(notas)
    boletim['mediaNotas'] = media(notas)
    if sit:
        boletim['situação'] = situacao(boletim['mediaNotas'])
    return boletim


print("-"*25)
print(notas(3.5,2.5,10,6.5,sit=True))
#help(notas)



