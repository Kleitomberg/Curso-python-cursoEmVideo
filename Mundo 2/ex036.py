print("====== DESAFIO 36 ======")

valorCasa = float(input("Qual valor da casa: R$ "))
salaro = float(input("Qual seu salário: R$ "))
tempo = int(input("Em quantos anos pretende pagar: "))

parcelas = valorCasa/(tempo*12)
regra = salaro*(30/100)

if parcelas > regra:
    print("Você não pode efetuar essa compra pois as parcelas de R${:.2f} exedem 30% que é R${:.2f} do seu salário".format(parcelas, regra))

elif parcelas <= regra:
    print("Boa compra, você terá que pagar {} vezes de R${:.2f} ".format(tempo*12, parcelas))