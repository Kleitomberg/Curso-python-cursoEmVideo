#print("====== DESAFIO 56 ======")

soma = 0
menosDeVinte = 0
maior = 0

for i in range(1,5):
    print("\nCADATRAR {}ª PESSOA".format(i))
    n = input("Digite o nome da {} pessoa: ".format(i)).title().strip()
    ida = int( input("Digite a idade da {} pessoa: ".format(i)))
    s = input("Informe o sexo da {} pessoa | F - Feminino e M - Masculino".format(i)).title().strip()

    soma = soma+ida

    if s == "M":
        if ida > maior:
            maior = ida
            nm = n
    elif s == "F":
        if ida < 20:
            menosDeVinte = menosDeVinte + 1

print("\nA media das idades é igual {}".format(soma/4))
print("O Homem com a maior idade é {} com {} anos".format(nm, maior))
print("{} Mulheres possuem menos de 20 anos".format(menosDeVinte))



