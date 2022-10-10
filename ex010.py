print("====== DESAFIO 10 ======")

carteiraBR = float(input('Quantos R$ Você possui? '))
dolaUS = float(4.77)
euro = float(5.14)

valoremDolar = carteiraBR/dolaUS
valoremEuro= carteiraBR/euro

print('A conversão do seus R${:.2f} em dola é igual a US${:.2f}\n e em Euro é «€»{:.2f}' .format(carteiraBR, valoremDolar, valoremEuro ))

