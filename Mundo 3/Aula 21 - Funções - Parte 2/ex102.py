#DESAFIO 102

def fatorial(num,show=False):
    """
    :param num:Representa o numero que sera calculado o fatorial
    :param show: define se sera mostrado o calculo ou apenas o resultado
    :return: retonar o fatorial do numero passado (f)
    """
    cont = num
    f = 1
    while cont >= 1:
        if show:
            print(f"{cont}",end='')
            if cont >=2:
                print(" x ",end='')
            elif cont == 1:
                print(' = ',end='')
        f *= cont
        cont-=1
    return f

numero = int(input("Qual numero deseja calcular ofatorial: "))

print(fatorial(numero, True))
#help(fatorial)

