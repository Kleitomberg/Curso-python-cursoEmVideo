import moeda

print("="*30)
valor = float(input("Qual o valor em R$:  "))
print("="*30)
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"Aumentar 10% em {moeda.moeda(valor)} = {moeda.moeda(moeda.aumentar(valor,10))}")
print(f"Desconto de 13% em {moeda.moeda(valor)} = {moeda.moeda(moeda.diminuir(valor,13))}")


