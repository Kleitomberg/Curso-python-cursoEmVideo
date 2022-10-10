# print("====== DESAFIO 65 ======")

continuar = "S"
maior = 0
soma = 0
digito = 0

while continuar == "S":
    number = int(input("Informe um numero: "))

    if digito == 0:
        menor = number
        maior = number

    else:
        if number < menor:
            menor = number

        if number > maior:
            maior = number

    soma = soma + number
    digito = digito + 1
    continuar = input("Quer continuar | S - sim N - Não: ").upper()[0].strip()

print("Você digitou {} numero e a media deles foi {}".format(digito, soma/digito))
print("O maior numero digitado foi {}".format(maior))
print("O menor numero foi {}".format(menor))
