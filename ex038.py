print("====== DESAFIO 38 ======")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print("{} O MAIOR que {}".format(n1, n2))
elif n2 > n1:
    print("{} é MAIOR que {}".format(n2,n1))
else:
    print(" tanto {} quanto {},são iguais".format(n1,n2))