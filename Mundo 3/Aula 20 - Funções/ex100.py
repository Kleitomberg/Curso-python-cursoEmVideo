#DESAFIO
from random import randint
from time import sleep

def sorteia():
    numeros = []
    for i in range(0,5):
        numeros.append(randint(1,10))
    print("Sorteando 5 valores para a lista: ", end='')
    for n in numeros:
        sleep(0.5)
        print(f"{n}, ", end="")
    print("PRONTO!")
    print("SOAMNDO OS VALORES...")
    sleep(1)
    somaPar(numeros)
def somaPar(lista):
    soma = 0
    for i,numero in enumerate(lista):
        if numero % 2 == 0:
            soma+=numero

    print(f"Somando os valores pares de {lista}, temos {soma}")

sorteia()


