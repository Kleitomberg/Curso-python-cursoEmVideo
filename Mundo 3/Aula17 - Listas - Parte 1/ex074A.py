print("DESAFIO 74")
print("-="*20)
print("MINHA RESPOSTA: ")
from random import randint

a1 = randint(1,10)
a2 = randint(1,10)
a3 = randint(1,10)
a4 = randint(1,10)
a5 = randint(1,10)

tupla = a1,a2,a3,a4,a5

maior = 0
for i in tupla:
    if i> maior:
        maior=i

if a1 < a2:
    menor = a1
else:
    menor = a2

for i in tupla:
    if i< menor:
        menor=i


print(f" Numeros sorteados: {tupla}")
print(f"O maior é: {maior}")
print(f"O Menor é: {menor}")

print("-="*20)

print("RESPOSTA DO VIDEO: ")

numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print("Os valores sorteados foram: ",end='')

for n in numero:
    print(f'{n} ', end='')

print(f'\nO Maior valor sorteado foi: {max(numero)}')
print(f"O Menor valor sorteado foi: {min(numero)}")
