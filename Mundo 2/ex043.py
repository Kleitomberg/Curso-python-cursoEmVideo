print("====== DESAFIO 43 ======")

peso = float(input("Qual seu peso em Kg: "))
altura = float(input("Qual sua altura em M: "))

imc = peso/altura**2

if imc < 18.5:
    print("Abaixo do peso | IMC = {:.1f}".format(imc))

elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal | IMC = {:.1f}".format(imc))

elif imc <=29.9:
    print("Sobrepeso | IMC = {:.1f}".format(imc))
elif imc <=40:
    print("Obesidade | IMC = {:.1f}".format(imc))
elif imc >40:
    print("Obesidade mórbida | IMC = {:.1f}".format(imc))



