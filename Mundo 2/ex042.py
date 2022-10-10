print("====== DESAFIO 42 ======")

from time import sleep

a = float( input("Digite o tamanho da reta 1 "))
b = float( input("Digite o tamanho da reta 2 "))
c = float( input("Digite o tamanho da reta 3 "))

# PODE SER a 12, b = 6  e c = 9
# NÃO PODE SER a 12 , b = 5 cm e c = 6 cm.
# a5 b 10 c 9

print("Processando...")

sleep(2)

if (abs(b - c) < a < b + c) or (abs(a - c) < b < a + c) or (abs(a - b) < c < a + b):

    if a==b==c:
        print("O Triangulo é Equilátero")
    elif a==b or a==c or c==b:
        print("O Triangulo é Isósceles")
    else:
        print("O Triangulo é Escaleno")
else:
    print("\nNÃO PODE SER TRINANGULO")
