print("====== DESAFIO 37 ======")
from time import sleep

print("\033[1:33mConversor Numerico\033[m")

mensagem ="Carregando..."

print("\033[0:30m{}\033[m".format(mensagem))
sleep(1)

valor = int(input("\nQual numero deseja converter: "))

print("\033[0:34mEscolha a para qual base deseja fazer a conversão do numero {}\033[m".format(valor))

print("\033[0:34m1 \033[m- \033[0:31mBinária \033[m")
print("\033[0:34m2 \033[m- \033[0:31mOctal \033[m")
print("\033[0:34m3 \033[m- \033[0:31mHexadecimal \033[m")

base = int(input('Digite a opção desejada: '))

if base==1:
    print("\033[0:32mConvertendo valor {} para Binario...\033[m".format(valor))
    sleep(2)
    print("\n \033[1:34mO valor {} em base binaria é igual a {}".format(valor, format(valor, "b")))
elif base==2:
    print("\033[0:32mConvertendo valor {} para Octal...\033[m".format(valor))
    sleep(2)
    print("\n \033[1:34mO valor {} em octal eqivale a {}".format(valor, format(valor, "o")))
elif base==3:
    print("\033[0:32mConvertendo valor {} para Hexadecimal...\033[m".format(valor))
    sleep(2)
    print("\n \033[1:34mO valor {} em Hexadecimal vale {}".format(valor, format(valor, "x").upper()))

elif base <=0 or base >=4:
    print("\033[1:31mError! Escolha uma base válida!\033[m")