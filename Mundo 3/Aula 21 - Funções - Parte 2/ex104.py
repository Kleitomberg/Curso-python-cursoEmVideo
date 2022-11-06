#DESAFIO 104

def leiaint(msg):

    while True:
        n = input(f"{msg}")

        if n.isnumeric():
            break
        else:
            print("\033[1;31m Error! Digite um numero válido!\033[0m")
    print("-="*30)

    return n

numero = leiaint("Digite um numero: ")
print(f"Você digitou o numero {numero}")
