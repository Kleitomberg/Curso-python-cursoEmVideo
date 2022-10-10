print("====== DESAFIO 28 ======")
from random import randint

from time import  sleep

aleatorio = randint(0,5)
print("-=-" *20)
print("Qual numero vai ser sorteado? ADVINHE AI!")
print("-=-" *20)

escolhido = int(input("DE 1 a 5, qual numero foi o sorteado? "))

print("Processando...")
sleep(3)
if aleatorio == escolhido:
    print("ACERTOUUU! O numero sortedo foi {}".format(aleatorio))
else:
    print("ERROOUUU! O numero sorteado foi {} e não {}. tente outra vez!".format(aleatorio, escolhido))
