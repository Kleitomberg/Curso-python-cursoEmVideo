print("====== DESAFIO 12 ======")

precoAtual = float(input('Digite o preço atual: '))
desconto = precoAtual*(5/100)
precoComDesconto = precoAtual-desconto

print('Um produto que custa {:.2f}R$ com desconto de 5% fica por {:.2f}R$\n O desconto equivale a {:.2f}R$ ' .format(precoAtual, precoComDesconto, desconto))