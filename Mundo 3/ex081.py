#desafio 81

numeros = []

while True:

    numeros.append(int(input("Digite um numero: ")))

    resposta = input("Quer continuar? S/N: ").upper()
    if resposta == 'N':
        break

print(f"Você digitou {len(numeros)} numeros, sendo eles: {numeros}\n")

print("Ordem decrescente")
numeros.sort(reverse=True)
print(numeros)

if 5 in numeros:
    print(f"O numero 5 foi digitado {numeros.count(5)}x! nas posições: ", end='')

for pos,v in enumerate(numeros):
    if v == 5:
        print(f"{pos}-1 ",end='')
