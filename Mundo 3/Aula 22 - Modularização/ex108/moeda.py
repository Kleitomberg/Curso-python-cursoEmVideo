def aumentar(dinheiro=0,aumento=0):
    if aumento != 0:
        aumento = dinheiro*(aumento/100)
    resultado = dinheiro+aumento
    return resultado


def diminuir(dinheiro=0, dedsconto = 0):
    if dedsconto != 0:
        dedsconto = dinheiro*(dedsconto/100)
    resultado = dinheiro-dedsconto
    return resultado


def dobro(dinheiro=0):
    resultado = 2 * dinheiro
    return resultado


def metade(dinheiro=0):
    resultado = dinheiro / 2
    return resultado


def moeda(dinheiro=0, moeda='R$'):
    return f"{moeda}{dinheiro:.2f}".replace('.',',')

