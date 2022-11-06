import moeda

print("="*30)
valor = float(input("Qual o valor em R$:  "))
print("="*30)
print(f"O dobro de {valor} é {moeda.dobro(valor)}")
print(f"A metade de {valor} é {moeda.metade(valor)}")
print(f"Aumentar 10% em {valor} = {moeda.aumentar(valor,10)}")
print(f"Desconto de 13% em {valor} = {moeda.diminuir(valor,13)}")


