print("====== DESAFIO 44 ======")
print("\033[1:36m--=\033[m"*10)
print(" "*12 + "Caixa")
print("\033[1:36m--=\033[m"*10)
valor = float(input("Qual valor do produto em R$: "))

print("\n\033[1:36mFormas de Pagamento:\033[m")
print( "[ 1 ] À vista no Dinheiro")
print( "[ 2 ] À vista no Cartão")
print( "[ 3 ] 2x no Cartão")
print( "[ 4 ] 3x ou mais no Cartão")

forma = int(input("\033[1:33mEscolha a forma de pagamento: \033[m"))

if forma ==1:
    print("\n\033[1:31mPagar à vista no Dinheiro\033[m")
    valorf = valor - (valor*(10/100))
    print("\033[1:34mSua compra de \033[1:32mR${:.2f}\033[m \033[1:34mCom\033[m \033[1:31m10%\033[m \033[1:34mde desconto o Valor a ser pago será\033[m \033[1:32mR${:.2f}\033[m".format(valor,valorf))
elif forma ==2:
    print("\033[1:31mPagar à vista no Cartão\033[m")
    valorf = valor - (valor*(5/100))

    print("\033[1:31mCom desconto de \033[m\033[1:31m5%\033[m\033[1:34m, o produto de\033[m \033[1:32mR${:.2f}\033[m, \033[1:34mpassa a valer \033[m\033[1:32mR${:.2f}\033[m".format(valor, valorf))

elif forma ==3:
    print("\033[1:31mpagar em 2x no Cartão\033[m")
    valorf = valor
    parcelar = valorf / 2
    print("\033[1:34mDeverá ser pago 2X de R${} os\033[m \033[1:31mR${:.2f}\033[m \033[1:34mque vale o produto".format(parcelar,valorf))
elif forma ==4:
    print("\033[1:31mpagar em 3x ou mais no Cartão\033[m")
    parcelas = int(input("pagar em quantas vezes: "))
    valorf = valor + (valor*(20/100))
    pagar = valorf/parcelas
    print("\033[1:34mCom\033[m \033[1:31m20%\033[m \033[1:34mde juros o valor aumenta de\033[m \033[1:32mR${}\033[m \033[1:34mpara\033[m \033[1:32mR${}\033[m".format(valor, valorf))
    print("Você irá pagar {} parcelas de R${:.2f}".format(parcelas,pagar))