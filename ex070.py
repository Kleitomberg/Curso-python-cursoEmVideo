# print("====== DESAFIO 70 ======")
from time import sleep
quantProd = total = maisMil = maisBarato = 0
produtoMb=""

print("-"*20)
print("       CAIXA      ")
print("-"*20)
while True:
    produto = input("Nome do produto: ")
    preco = float(input(f"Valor do(a) {produto} R$: "))

    sleep(1)
    print("\033[1:32mProduto adicionado!\033[m")
    quantProd+=1

    if quantProd == 1:
        maisBarato = preco
        produtoMb = produto


    else:
        if preco < maisBarato:
            maisBarato = preco
            produtoMb = produto

    total = total+ preco
    if preco > 1000:
        maisMil += 1

    sleep(0.5)
    continua = " "
    while continua not in "SN":
     continua = input("Adicionar outro produto? S Sim  | N - Não ").title().strip()[0]
    print("-" * 20)
    if continua =="N":
        break


print("\nResumo da compra")

print(f"Você comprou {quantProd} produtos, {maisMil} custando mais de R$ 1000.00 ")
print(f"Total da compra = {total:.2f}")
print(f"O Produto mais barato foi o(a){produtoMb} custando R${maisBarato:.2f}")
