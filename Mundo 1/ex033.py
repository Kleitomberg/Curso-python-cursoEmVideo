print("====== DESAFIO 33 ======")

n1 = int( input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int( input("Numero 3: "))

if n1>n2 and n1>n3:
    maior = n1
    print("O maior é o numero {}".format(n1))

if n2>n1 and n2>n3:
    maior = n2
    print("O maior é o numero {}".format(n2))

if n3>n1 and n3>n2:
    maior = n3
    print("O maior é o numero {}".format(n3))

if n1<n2 and n1<n3:
    menor = n1
    print("O Menor é o numero {}".format(n1))

if n2<n1 and n2<n3:
    menor = n2
    print("O Menor é o numero {}".format(n2))

if n3<n1 and n3<n2:
    menor = n3
    print("O Menor é o numero {}".format(n3))