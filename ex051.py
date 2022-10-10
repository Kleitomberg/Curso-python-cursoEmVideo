#print("====== DESAFIO 51 ======")


inicial = int(input("valor inicial: "))
razao = int(input("razão: "))
sequencia = []
prox = 0

ultimo = (inicial+(10-1)*razao)+1

for i in range(inicial, ultimo, razao):
   #print(i)
   # sequencia.append(i)
   print("{}".format(i),end=" -> ")
#print("A sequencia é {}".format(sequencia))
