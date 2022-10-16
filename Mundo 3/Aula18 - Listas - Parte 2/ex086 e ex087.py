#DESAFIO 86
'''
soma = 0
somaT = 0
maiorS = 0
matriz = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]  = int(input(f"Digite um valor para {(i,j)}: "))


for loluna in matriz[0]:
    print(f" [ {loluna} ] ", end='')
print("")
for pos,loluna in enumerate(matriz[1]):
    print(f" [ {loluna} ] ", end='')

    if pos ==0:
        maiorS = loluna
    else:
        if loluna > maiorS:
            maiorS = loluna
print("")
for loluna in matriz[2]:
    print(f" [ {loluna} ] ", end='')
    somaT+=loluna

for i in range(0, len(matriz)):
    for valor in matriz[i]:
        if valor%2==0:
            soma +=valor



print(f"\nSoma de pares: {soma}")
print(f"Soma 3° Coluna: {somaT}")
print(f"Maior 2° Coluna: {maiorS}")

'''
print("_"*20)

#RESPOSTA PÓS VIDEO

somaPares = somaTerceira = maiorLinha  = 0
matrizV = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matrizV[linha][coluna]  = int(input(f"Digite um valor para {(linha,coluna)}: "))
print("-="*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f' [{matrizV[linha][coluna]:^5}] ', end='')

        if coluna == 2:#terfceira coluna
            somaTerceira+=matrizV[linha][coluna]

        if matrizV[linha][coluna] % 2 == 0: #pares
            somaPares+= matrizV[linha][coluna]

        if linha == 1: # 2° Linha
            if coluna == 0:#primeiro elemento da linha
                maiorLinha = matrizV[linha][coluna]
            else:
                if maiorLinha < matrizV[linha][coluna]:
                    maiorLinha = matrizV[linha][coluna]
    print()

print("-="*30)

print(f" Soma de pares {somaPares}")
print(f" Soma terceira coluna {somaTerceira}")
print(f" Maior valor da 2° Linha  {maiorLinha}")
