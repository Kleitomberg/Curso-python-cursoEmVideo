#print("====== DESAFIO 57 ======")

'''Python 57: Faça um programa que leia o sexo de uma pessoa,
 mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça
 a digitação novamente até ter um valor correto.
'''
sexo = input("Infome o sexo | F - Feminino | M - Masculino: ").upper().strip()[0]
while sexo !="M" and sexo !="F":
    print("\nValor invalido! por favor digite novamente! ")
    sexo = input("Infome o sexo | F - Feminino | M - Masculino: ").upper().strip()[0]


print("Sexo {} cadastrado com sucesso!".format(sexo))

