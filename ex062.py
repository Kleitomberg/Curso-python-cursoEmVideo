#print("====== DESAFIO 62 ======")

inicial = int(input("valor inicial: "))
razao = int(input("razão: "))

tottermos = 10
controle = 10

while controle >0: # entre  10 - 1

   print("{}".format(inicial),end=" -> ")
   inicial = inicial + razao
   controle -=1

   #Se o controle chegou em 0 significa que já foram exibidos os 10 primeiros termos
   if controle == 0:
      acrescimo = int(input("\nQuantos termos deseja exibir além dos 10 + "))
      print("pausa")
      controle = acrescimo
      tottermos = tottermos+acrescimo

print("FIM! foram exibidos os {} primeiros termos".format(tottermos))