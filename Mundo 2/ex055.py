#print("====== DESAFIO 55 ======")

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input("Digite o peso da {} pessoa: " .format(i)))

    if i == 1:
        maior = peso
        menor = peso

    else:

        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso


print("O MENOR peso entre os 5 foi {:.2f}Kg".format(menor))
print("O MAIOR peso foi de {:.2f}Kg".format(maior))