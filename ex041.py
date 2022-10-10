print("====== DESAFIO 41 ======")

from datetime import date

nascimento = int(input("Em qual ano você nasceu: "))

idade = abs(nascimento - date.today().year)

if idade <=9:
    print("\033[1:36mMIRIM\033[m idade = {}".format(idade))
elif idade >=10 and idade<=14:
    print("\033[1:35mINFANTIL\033[m idade = {}".format(idade))
elif idade<=19:
    print("\033[1:33mJUNIOR\033[m idade = {}".format(idade))
elif idade<=25:
    print("\033[1:32mSÊNIOR\033[m idade = {}".format(idade))
else:
    print("\033[1:31mMASTER\033[m idade = {}".format(idade))


