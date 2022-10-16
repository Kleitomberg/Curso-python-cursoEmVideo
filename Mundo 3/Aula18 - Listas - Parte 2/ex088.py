#DESAFIO 88

from random import randint
from time import sleep
"""
jogos = []
jogo = []
quantidade = int(input("Quantos jogos deseja sortear? "))

for i in range(0, quantidade):
    for i in range(0,6):
        numero = randint(0,60)
        jogo.append(numero)

    jogos.append(jogo[:])
    jogo.clear()
print("Sorteando Jogos...")
for pos,j in enumerate(jogos):
    sleep(1)
    print(f"Jogo {pos+1} = {j}")

sleep(0.9)
print("BOA SORTE ")
"""
#RESPOSTA PÓS VIDEO
print("-"*30)
print("      JOGAR NA MEGA SENA      ")
print("-"*30)
jogos = []
jogo = []
quantidade = int(input("Quantos jogos deseja sortear?: "))
for i in range(0, quantidade):
    while True:
        numero = randint(0,60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) >=6:
            jogos.append(jogo[:])
            break
    jogo.clear()
print()
print("-="*3, f'SORTEANDO {quantidade} jogos ', '-='*3)
for pos,j in enumerate(jogos):
    sleep(1)
    print(f"JOGO {pos+1} = {sorted(j)}")

