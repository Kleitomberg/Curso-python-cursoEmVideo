print("====== DESAFIO 32 ======")

from datetime import date

ano = int( input("Digite um ano: use 0 para pegar ano atual ") )

m100 = ano % 100 != 0

if ano == 0:
    ano = date.today().year

if ano%4==0 and ano % 100 != 0 or ano % 400 == 0 :
    print("{} É um ano bissexto".format(ano))
else:
    print("{} Não é um ano bissexto".format(ano))