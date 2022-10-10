#desafio 82

numeros = []
pares = []
impares = []

while True:

    numeros.append(int(input("Digite um valor: ")))

    resposta = input("Quer continuar? S/N: ").upper()

    if resposta == 'N':
        break

for v in numeros:
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)

print(f"\nLista completa = {numeros}")
print(f"\nOs pares = {pares}")
print(f"\nOs Impares = {impares}")

