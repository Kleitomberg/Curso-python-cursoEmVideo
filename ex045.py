# print("====== DESAFIO 44 ======")
from time import sleep
from random import randint
import emoji


print(" " * 10 + "\033[1:35m\033[m\033[1:35m🎮\033[m\033[1:33mJokenpy\033[m\033[1:35m🎮\033[m")

print("\033[1:34mVamos jogar pedra, papel e tesoura!\033[m\n")

sleep(0.9)

print("\033[1:31mEai qual vai escolher:\033[m")
print("\033[1:35m1\033[m - \033[1:33mPedra\033[m ")
print("\033[1:35m2\033[m - \033[1:33mPapel\033[m ")
print("\033[1:35m3\033[m - \033[1:33mTesoura\033[m ")

eu = int(input("\033[1:35mFaça a sua jogada: \033[m"))
computador = randint(1, 3)

score = 0
opcoes = ["invalidado","Pedra", "Papel", "Tesoura"]

#Cores
fechamento = "\033[m"
branco = "\033[1:30m"
azul = "\033[1:34m"
vermelho = "\033[1:31m"
verde = "\033[1:32m"
amarelo = "\033[1:33m"
roxo = "\033[1:35m"


sleep(0.5)
print("\n\033[1:35mJO\033[m ",end="")
sleep(0.7)
print("\033[1:33mKEN\033[m ",end="")
sleep(1)
print("\033[1:35mPY!!!\033[m")
sleep(0.6)
if (eu == 1 and computador == 3) or (eu == 2 and computador == 1) or (eu == 3 and computador == 2):

    print(emoji.emojize("\n\033[1:33m :1st_place_medal:\033[m \033[1:32mV I T O R I A!\033[1:33m :1st_place_medal:\033[m \033[m\n \033[1:34mVocê\033[m jogou {}{}{} e \033[1:31mCOM\033[m jogou {}{}{} ".format(amarelo, opcoes[eu], fechamento, amarelo, opcoes[computador], fechamento)))
    score = score + 1
    print("Pontos: {} pontos".format(score))
elif (eu == 1 and computador == 2) or (eu == 2 and computador == 3) or (eu == 3 and computador == 1):

    print(emoji.emojize("\n\033[1:37m :2nd_place_medal:\033[m \033[1:31mD E R R O T A!\033[1:37m :2nd_place_medal:\033[m \033[m\n \033[1:34mVocê\033[m jogou {}{}{} e \033[1:31mCOM\033[m jogou {}{}{} ".format(amarelo, opcoes[eu], fechamento, amarelo, opcoes[computador], fechamento)))

elif (eu == 1 and computador == 1) or (eu == 2 and computador == 2) or (eu == 3 and computador == 3):
    print("\033[1:33m\nE M P A T E!\033[m\n \033[1:34mVocê\033[m jogou {}{}{} e \033[1:31mCOM\033[m também jogou {}{}{}".format(amarelo, opcoes[eu], fechamento, amarelo, opcoes[computador], fechamento))
