#DESAFIO 89
"""
alunos =[]
dados = []
nome = []
notas = []
soma = 0
while True:

    nome.append(str(input("Nome: ")))
    notas.append(float(input("NOTA 1: ")))
    notas.append(float(input("NOTA 2: ")))
    dados.append(nome[:])
    dados.append(notas[:])
    alunos.append(dados[:])
    dados.clear()
    nome.clear()
    notas.clear()

    resposta = str(input("Quer continuar? S/N: ")).upper()
    if resposta == 'N':
        break


print("-="*20)


for pos,a in enumerate(alunos):

    for nota in range(0, len(a[1])):
        soma = soma + a[1][nota]
        if nota == 1:
            a[1].append(soma / 2)
            soma = 0

print("#         Nome          Média")
print("_"*30)
for pos,a in enumerate(alunos):
    print(f"\n{pos}°     {a[0][0]}            {a[1][2]}")

print("_"*30)

while True:
    opcao = int(input("De qual aluno deseja mostrar as notas? (999 = FIM): "))
    print(alunos[opcao])

    if opcao == 999:
        break
"""
#RESPOSTA PÓS VER O VIDEO DE SOLUÇÃO

alunos = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    alunos.append([nome,[nota1,nota2], media])

    resposta = str(input("Quer continuar? S/N: ")).upper()
    if resposta in 'Nn':
        break
print(f"-="*30)

print(f'{"N°.":<4}{"Nome":<10}{"Média":>10}')
print("-"*26)
for pos,aluno in enumerate(alunos):
    print(f"{pos:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

print("_"*30)

while True:
    opcao = int(input("De qual aluno deseja mostrar as notas? (999 = FIM): "))

    if opcao < 0 or opcao >= len(alunos):
        print(f"NENHUM ALUNO ENCONTRADO NA POSIÇÃO {opcao}")
    else:
        print(f"As notas de {alunos[opcao][0]} foram {alunos[opcao][1]}")
    if opcao == 999:
        break
