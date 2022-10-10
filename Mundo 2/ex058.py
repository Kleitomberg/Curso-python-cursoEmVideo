#print("====== DESAFIO 58 ======")

'''
Python 58: Melhore o jogo do DESAFIO 28
onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
import emoji
from time import sleep

continuar = 11
tentativa = 0
aleatorio = randint(0, 10)

while continuar != aleatorio:

    tentativa =tentativa+1
    print(" ")
    print("-=-" *20)
    print("Qual numero vai ser sorteado? ADVINHE AI!")
    print("-=-" *20)

    escolhido = int(input("DE 1 a 10, qual numero foi o sorteado? "))
    continuar = escolhido
    print("Processando...")
    sleep(1)
    if aleatorio == escolhido:
        print("\nACERTOUUU! \nO numero sortedo foi {}".format(aleatorio))
    else:
        print("\nERROOUUU! \nO {} não foi o sorteado. tente outra vez!".format(escolhido))
        if escolhido > aleatorio:
            print(emoji.emojize(':light_bulb: Dica: Tente um valor Menor'))
        else:
            print(emoji.emojize(':light_bulb: Dica: Tente um valor Maior'))

print("PARABÉNS, VOCÊ ACERTOU EM {} tentativas ".format(tentativa))