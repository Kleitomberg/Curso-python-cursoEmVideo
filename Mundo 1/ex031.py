print("====== DESAFIO 31 ======")

distancia = float(input("Qual a distancia: "))
preco=0
if distancia <=200:
    preco = distancia*0.50
    print("Em uma viagem de {}Km, você devera pagar R${}".format(distancia, preco))
else:
    preco = distancia*0.45
    print("Em uma viagem de {}Km, você devera pagar R${}".format(distancia, preco))