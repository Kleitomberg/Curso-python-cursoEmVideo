import moeda

print("="*30)
valor = float(input("Qual o valor em R$:  "))
print("="*30)
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,format=True)}")
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor,format=True)}")
print(f"Aumentar 10% em {moeda.moeda(valor)} = {moeda.aumentar(valor,10,format=True)}")
print(f"Desconto de 13% em {moeda.moeda(valor)} = {moeda.diminuir(valor,13, format=True)}")


