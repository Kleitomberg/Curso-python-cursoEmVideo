#print("====== DESAFIO 52 ======")
numero = int(input("Digite um numero: "))
isprimo = True

if numero > 1:
    for i in range(1,numero+1):
        if i != 1 and i != numero:
            if numero % i == 0:
                isprimo =False

elif numero ==1:
    print("O numero 1 não é primo")

if numero != 1:
    if isprimo == True:
        print("{} É primo".format(numero))
    elif isprimo == False:
        print("{} NÃO é primo".format(numero))