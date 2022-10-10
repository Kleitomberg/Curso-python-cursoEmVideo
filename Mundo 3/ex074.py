# print("====== DESAFIO 72 ======")
maior = 0
menor = 9999
from random import randint

turtle = (randint(0,999),randint(0,999),randint(0,999),randint(0,999),randint(0,999))


if randint(0,999) < menor:
    menor = randint(0, 999)

if randint(0, 999) > maior:
    maior = randint(0, 999)


print(turtle)
print(f'Maior {maior}')
print(f'Menor {menor}')