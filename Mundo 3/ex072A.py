print("____________DESAFIO 072_______________")

numeros = ("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete",
           "Oito","Nove","Dez","Onze","Doze","Treze","Catorze","Quinze",
           "Dezesseis","Dezessete","Dezoite","Dezenove","Vinte"
           )


while True:
    valor = int(input("Digite um valor de 0 a 20: "))
    if valor >= 0 and valor <= 20:
        print(f"{valor} - {numeros[valor]}")

        print("Quer conitnuar?")
        op = int(input("0 - Sim | 1 - Não: "))
        if op and op != 0:
            break
    else:
        print(f"{valor} = Valor invalido, por favor tente novamente!")

print("ACABAOU")
