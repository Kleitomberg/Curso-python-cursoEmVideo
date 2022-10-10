print("====== DESAFIO 13 ======")

salario = float(input('Meu Salário é: '))
aumento = salario*(15/100)
salarioComAumento = salario+aumento

print('Um Salário de {:.2f}R$ com aumento de 15% passará a ser {:.2f}R$\n Sendo assim o valor do aumento foi de {:.2f}R$' .format(salario, salarioComAumento, aumento))