#DESAFIO
from random import randint
from time import sleep

def sorteia():
    """
    FUNÇÃO SORTEAR SORTEIA 5 VALORES DE 1 A TÉ 10
    ADICIONA EM UMA LISTA NUMEROS
    E CHAMA A FUNÇÃO SOMARPARES QUE IRÁ SOMAR OS VALORES PARES DA LISTA

    :return:
    """
    numeros = []
    print("-="*40)
    for i in range(0,5):
        numeros.append(randint(1,10))
    print("Sorteando 5 valores para a lista: ", end='')
    for n in numeros:
        sleep(0.5)
        print(f"{n} ", end="")
    print("PRONTO!")
    print("-=" * 40)
    print("SOAMNDO OS VALORES...")
    print("-=" * 40)
    sleep(1)
    somaPar(numeros)


def somaPar(lista):
    sleep(0.5)
    soma = 0
    for i,numero in enumerate(lista):
        if numero % 2 == 0:
            soma+=numero
    print(f"Somando os valores pares de {lista}, temos {soma} no total")
#sorteia()


help(sorteia)
