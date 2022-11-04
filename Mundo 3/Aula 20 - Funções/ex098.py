#DESAFIO 98
from time import sleep
def contador(incio,fim,passo):
    print(f"Contagem de {incio} até {fim} de {abs(passo)} em {abs(passo)}")

    if passo == 0:
        passo = 1
    if incio < fim:
        for i in range(incio,fim+1,abs(passo)):
            sleep(0.5)
            print(f"{i} ", end='')
        print("FIM")
    elif incio > fim:

        for i in range(incio,fim-abs(passo),abs(passo)*-1):
            sleep(0.5)
            print(f"{i} ", end='')
        print("FIM")

#contador(1,10,1)
#contador(10,0,2)

print("-="*25)
print("Agora é a sua vez! Informe o intervalo da contagem desejada e o passo!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio,fim,passo)
