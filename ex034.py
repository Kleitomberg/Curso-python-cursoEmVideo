print("====== DESAFIO 34 ======")

salario = float(input("Qual seu salário: "))

if salario>1250:
    aumento = ((10/100)*salario)+salario
    print("Seu salário com 10% de aumento será de {}".format(aumento))
else:
    aumento = ((15/100)*salario)+salario
    print("Seu salário com 15% de aumento passará a ser {}".format(aumento))