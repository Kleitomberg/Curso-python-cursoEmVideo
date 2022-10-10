#print("====== DESAFIO 59 ======")

from time import  sleep

continuar = True
maior = 0

print("\nINFORME DOIS NUMEROS")
n1 = int(input("Digite 1º valor: "))
n2= int(input("Digite o 2º valor: "))
while continuar:

    print("\n === MENU === ")

    print("[ 1 ] Somar")
    print('[ 2 ] Multiplicar')
    print("[ 3 ] maior")
    print("[ 4 ] novos valores")
    print("[ 0 ] sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao ==1:
        soma = n1+n2
        print("SOMA")
        print("A soma entre {} e {} é {}".format(n1,n2,soma))

    elif opcao ==2:
        multi = n1*n2
        print("MULTIPLICAÇÃO")
        print("A Multiplicação entre {} e {} é {} ".format(n1,n2,multi))

    elif opcao == 3:
        print("MAIOR")
        if n1 > n2:
            maior = n1
            print("{} é maior que {}".format(n1, n2))
        elif n1 == n2:
            print("Não há maior, ambos são iguais")
        elif n2 > n1:
            maior=n2
            print("{} é maior que {}".format(n2,n1))
    elif opcao == 4:
        print("\nINFORME DOIS NOVOS NUMEROS")
        n1 = int(input("Digite 1º valor: "))
        n2 = int(input("Digite o 2º valor: "))
    elif opcao == 0:
        continuar = False

        print("Finalizando ...")
        sleep(2)

    else:
        print("Opção invalida, tente outra vez!")

    print("________________________")
    sleep(2)
print("FIM")