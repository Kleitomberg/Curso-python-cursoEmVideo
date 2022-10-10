#Desafio 78

numeros = []
posicao = []

for i in range(0,5):
  numeros.append(int(input(f"Informe um valor para a posição {i}: ")))

print("-="*20)
print(f"Você digitou {numeros}")

for pos,valor in enumerate(numeros):
    if pos == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor




print(f"O MAIOR valor foi: {maior} na posição ",end='')

for i,n in enumerate(numeros):
    if n == maior:
        print(f" {i} ",end='')



print(f"\nO MENOR valor foi: {menor} nas posições ", end='')

for i,n in enumerate(numeros):
    if n == menor:
        print(f" {i} ",end='')
