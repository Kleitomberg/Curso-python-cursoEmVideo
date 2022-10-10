# print("====== DESAFIO 66 ======")

digitos = 0
soma = 0
continuar = True

while continuar:

    numero = int(input("Informe um numero | 999 para parar: "))
    if numero == 999:
        break
    soma = soma + numero
    digitos = digitos + 1


print(f"digitou {digitos} numero e a soma é {soma}")



