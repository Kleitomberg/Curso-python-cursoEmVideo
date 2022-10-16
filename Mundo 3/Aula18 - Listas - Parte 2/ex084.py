#desafio 84

dados = []
i = 1
pessoas = []
maior = menor = 0
print("-=" * 20)
print("CADASTRAR PESSOAS")
print("-=" * 20)
while True:
    print(f"Pessoa {i}")
    dados.append(str(input(f"Nome: ")))
    dados.append(float(input("Peso: ")))
    print("-" * 20)
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input("Quer Continuar? S/N: ")).upper()
    i+=1
    if resposta == 'N':
        break
print(f"Pessoas cadastradas: {len(pessoas)}")
for pos,p in enumerate(pessoas):
    if pos == 0:
        maior = menor = p[1]
    else:
        if p[1]> maior:
            maior =p[1]
        if p[1] < menor:
            menor =p[1]
print(f"O Maior pesso foi de {maior}Kg. Peso de ",end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}, ", end='')
print(f"\nO Menor pesso foi de {menor}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}, ", end='')


