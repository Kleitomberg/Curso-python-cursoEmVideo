#DESAFIO 79

numeros = []

while True:
    valor = int(input("Digite um valor: "))
    if not valor in numeros:
        print("Valor adicionado com sucesso!")
        numeros.append(valor)
    else:
        print("Valor já existe")
    resposta = input("Quer continuar: S/N : ").upper()
    if resposta == 'N':
        break
numeros.sort()
print(f"{numeros}")
