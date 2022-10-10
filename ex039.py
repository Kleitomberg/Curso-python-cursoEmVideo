print("====== DESAFIO 39 ======")

from datetime import date
anoatual = date.today().year
nascimento = int(input("Em que ano vocÊ nasceu: "))

idade = anoatual-nascimento

print("Digite F para Feminino e M para masculino")
sexo = input("Qual seu SEXO: ").title()

if sexo =="M":
    if idade < 18:
        print("Calma ainda não chegou a hora de se alistar, faltam {} anos".format(abs(18 - idade)))
        print("Seu alistamento será em {}".format(anoatual + abs(18 - idade)))
    elif idade == 18:
        print("Chegou a hora, se aliste já")
    elif idade > 18:
        print("Já passaram-se {} anos da hora de se alistar".format(abs(18 - idade)))
        print("Seu alistamento ocorreu em {}".format(anoatual - abs(18 - idade)))
elif sexo=="F":
    print("Mulheres não precisa se alistar")

else:
    print("Opção invalida")

