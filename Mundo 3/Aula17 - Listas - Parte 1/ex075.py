print("Desafio 75")


a1 = int(input("\n Digite o 1° valor: "))
a2 = int(input("Digite o 2° valor: "))
a3 = int(input("Digite o 3° valor: "))
a4 = int(input("Digite o 4° valor: "))

tupla = a1,a2,a3,a4

print(f"\nVocê digitou os valores: {tupla}")
print(f"O VALOR 9 APARECE : {tupla.count(9)} vezes")

if (tupla.count(3)!= 0):
    print(f"O VALOR 3 APARECE pela primeira vez na posição: {tupla.index(3)+1} ")
else:
    print("O valor 3 não foi digitado nenhuma vez")

print(f"São pares:", end='')
for p in tupla:
    if p%2==0:
        print(f"{p} ",end='')
print("")
print("-="*20)
print("RESPOSTA DO VIDEO: ")

numeros = (
int(input("\n Digite o 1° valor: ")),
int(input("\n Digite o 2° valor: ")),
int(input("\n Digite o 3° valor: ")),
int(input("\n Digite o 4° valor: ")),
)
print(f" Você digitou os valor {numeros}")
print(f"O VALOR 9 APARECE : {numeros.count(9)} vezes")

if 3 in numeros:
    print(f"O VALOR 3 APARECE pela primeira vez na posição: {numeros.index(3) + 1} ")
else:
    print("O valor 3 não foi digitado nenhuma vez")

print(f"São pares:", end='')
for num in numeros:
    if num%2==0:
        print(f"{num} ", end='')
