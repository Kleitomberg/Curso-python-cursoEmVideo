print("====== DESAFIO 29 ======")

velocidade = float(input("Velocidade: "))

if velocidade>80:
    print("AVISO!\nVocê ultrapassou o limite de velocidade de 80KM Fazendo {}km amais \nDevera pagar o valor de R${:.2f} de multa".format(velocidade-80, (velocidade-80)*7 ))
else:
    print("Bom dia, continue dirigindo com segurança")