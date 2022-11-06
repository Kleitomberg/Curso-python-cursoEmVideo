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
