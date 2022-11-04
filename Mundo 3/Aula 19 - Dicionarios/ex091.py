#Desafio 091

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = {}

input(" Precione qualquer tecla para começar ")
for i in range(1,5):
    jogadores[f'jogador {i}'] = randint(1,6)
print()

print("Valores Sorteados")
for k,v in jogadores.items():
    print(f"{k} tirou {v}")
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #Ordenandoo dicionario
print("-="*20)
print(" == RANKING DE MAIORES PONTUADORES! == ")


for i,jogador in enumerate(ranking):
    print(f" {i+1}° Lugar -  {jogador[0]} | pontos = {jogador[1]}")
    sleep(1)
