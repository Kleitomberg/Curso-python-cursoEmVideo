# print("====== DESAFIO 69 ======")

totcadatros = maisDzoito = homens = mulheres = mulheresMenosVinte = 0

while True:
    print("-"*20)
    print("Cadastrar usuario!")
    print("-" * 20)

    idade =int(input("Idade: "))
    sexo = " "
    while sexo != "M" and sexo != "F":
        sexo = input("Sexo: M - Masculino | F - Feminino: ").strip().title()[0]
    totcadatros = totcadatros+1

    if idade >18:
        maisDzoito+=1

    if sexo == "M":
        homens+=1

    if sexo =="F":
        mulheres+=1
        if idade <20:
            mulheresMenosVinte+=1

    print(" \033[1:32mPessoa cadastrada!\033[m")
    continuar=" "
    while continuar not in "SN":
        continuar = input("Quer continuar? S - Sim | N - Não: ").strip().title()[0]
    if continuar =="N":
        break

print("-"*20)
print("\nRelatorio final")

print(f"foram cadastradas: {totcadatros} pessoas")
print(f"Mais de 18 anos: {maisDzoito} pessoas")
print(f"Homens: {homens} ")
print(f"Mulheres: {mulheres} ")
print(f"Mulheres com menos de 20 Anos: {mulheresMenosVinte} Mulheres")