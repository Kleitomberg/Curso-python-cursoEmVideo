from utils import moeda,dados
print("="*30)
valor = dados.leiaDinheiro("Qual o valor em R$: ")
print("="*30)
moeda.resumo(valor,20,12)

