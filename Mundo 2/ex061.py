#print("====== DESAFIO 61 ======")

inicial = int(input("valor inicial: "))
razao = int(input("razão: "))

controle = 1

while controle <=10:
   print("{}".format(inicial),end=" -> ")
   inicial = inicial + razao
   controle +=1

print("Fim")