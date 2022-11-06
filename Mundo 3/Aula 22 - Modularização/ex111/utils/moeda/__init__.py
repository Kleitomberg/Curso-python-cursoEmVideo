def aumentar(dinheiro=0,aumento=0, format=False):
    if aumento != 0:
        aumento = dinheiro*(aumento/100)
    resultado = dinheiro+aumento
    if format:
        return moeda(resultado)
    else:
        return resultado


def diminuir(dinheiro=0, dedsconto = 0, format=False):
    if dedsconto != 0:
        dedsconto = dinheiro*(dedsconto/100)
    resultado = dinheiro-dedsconto
    if format:
        return moeda(resultado)
    else:
        return resultado


def dobro(dinheiro=0, format=False):
    resultado = 2 * dinheiro
    if format:
        return moeda(resultado)
    else:
        return resultado


def metade(dinheiro=0, format=False):
    resultado = dinheiro / 2
    if format:
        return moeda(resultado)
    else:
        return resultado



def moeda(dinheiro=0, moeda='R$'):
    return f"{moeda}{dinheiro:.2f}".replace('.',',')


def resumo(dinheiro = 0, aumento = 10, desconto = 5):
    print("-"*40)
    print(f"RESUMO GERAL".center(40))
    print("-"*40)
    print(f"Valor inicial: \t\t{moeda(dinheiro)}")
    print(f"Dobro: \t\t\t\t{dobro(dinheiro,format=True)}")
    print(f"Metade: \t\t\t{metade(dinheiro,True)}")
    print(f"{desconto}% de desconto: \t{diminuir(dinheiro,desconto,True)}")
    print(f"{aumento}% de aumento: \t{aumentar(dinheiro,aumento,True)}")
