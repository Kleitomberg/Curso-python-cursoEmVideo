#print("====== DESAFIO 50 ======")

pares = []
soma = 0
for i in range(1,7):
    numero = int(input("Digite um numero: "))
    if numero%2==0:
        pares.append(numero)
        soma = soma+numero
        #print("{}".format(numero), end=" ")

print("Os pares digitados foram {}".format(pares))
print("A soma é deles é {}".format(soma))