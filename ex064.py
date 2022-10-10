#print("====== DESAFIO 64 ======")
soma = 0
contatdor = 0
numero = int(input("Digite um numero | 999 para parar : "))
while numero != 999 :
    contatdor+=1
    soma = soma+numero
    numero = int(input("Digite um numero: "))
print("Soma dos {} digitos foi de {}".format(contatdor,soma))