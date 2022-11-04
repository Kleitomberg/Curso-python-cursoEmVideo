#desafio 94

pessoas = []
dados = {}
soma = media = 0
while True:


    dados['nome'] = str(input("Nome: "))

    while True:
        dados['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if dados['sexo'] in 'MF':
            break

        print("Error! Apenas M ou F")

    dados['idade'] = int(input("Idade: "))
    pessoas.append(dados.copy())
    print("-="*20)
    print("Pessoa Cadastrada com sucesso!")
    print("-=" * 20)


    while True:
        resposta = str(input("Quer continuar? (S/N): ")).upper()[0]
        if resposta in 'SN':
            break
        print("Error! Apenas S ou N")

    if resposta in 'Nn':
        break

print()
print("-="*20)
print(f" Dados salvos ")
print("-="*20)
print()
print(f"Foram cadastradas {len(pessoas)} pessoas!")
print()
for p in pessoas:
   soma +=p['idade']

print(f"A Média de idade foi de {soma/len(pessoas)} anos")
print("As mulheres cadastradas foram: ", end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f"{p['nome']}, ",end='')
print()
print("LISTA DE PESSOAS COM IDADE A CIMA DA IDADE: ")

for p in pessoas:
    if p['idade'] >= soma/len(pessoas):
        print(f"Nome = {p['nome'] } | Sexo = {p['sexo']} | Idade = {p['idade']}")
print(' F I M ')
