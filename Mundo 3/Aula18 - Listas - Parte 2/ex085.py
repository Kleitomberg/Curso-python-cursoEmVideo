#DESAFO 85

numeros =[[],[]]

for i in range(0,7):
    numero = int(input("Digite um numero: "))
    if numero%2==0:
        numeros[1].append(numero)
    else:
        numeros[0].append(numero)

print(f"Os numero pares são: {sorted(numeros[1])}")
print(f"Os impares são: {sorted(numeros[0])}")

