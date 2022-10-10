# print("====== DESAFIO 71 ======")
notasD50 = notas20 = notas10 = notas1 = 0
print(" -- Kb Bank -- ")
saque = int(input("Quanto R$ gostaria de sacar? R$ "))
valor = saque
while True:
    if saque >=50:
        notasD50 = saque//50
        saque = saque%50

    elif saque >=20:
        notas20 = saque // 20
        saque = saque % 20

    elif saque >=10:
        notas10 = saque // 10
        saque = saque % 10

    elif saque >=1:
        notas1 = saque // 1
        saque = saque % 1

    elif saque ==0:
        break

print(f"Ao sacar R${valor} você receberá : ")
if notasD50 >0:
    print(f"{notasD50} notas de R$50")
if notas20 >0:
    print(f"{notas20} notas de R$20 ")

if notas10 >0:
    print(f"{notas10} notas de R$10")

if notas1 >0:
    print(f"{notas1} notas de R$1 e ainda falta")



