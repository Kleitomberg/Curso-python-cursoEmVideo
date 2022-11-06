def aumentar(dinheiro,aumento=0):
    if aumento != 0:
        aumento = dinheiro*(aumento/100)
    resultado = dinheiro+aumento
    return resultado


def diminuir(dinheiro, dedsconto = 0):
    if dedsconto != 0:
        dedsconto = dinheiro*(dedsconto/100)
    resultado = dinheiro-dedsconto
    return resultado


def dobro(dinheiro):
    resultado = 2 * dinheiro
    return resultado


def metade(dinheiro):
    resultado = dinheiro / 2
    return resultado
