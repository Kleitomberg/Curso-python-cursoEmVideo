#print("====== DESAFIO 54 ======")

from datetime import date

anoatual = date.today().year

maioridade =0
nmaioridade=0

for i in range(0,7):
    nascimento = int(input("Qual ano você nasceu: "))
    idade = anoatual-nascimento
    if idade >=21:
        maioridade= maioridade+1
    else:
        nmaioridade = nmaioridade+1

print("{} pessoas dos 7 já são maiores".format(maioridade))
print("{} pessoas dos 7 Ainda não são maiores".format(nmaioridade))