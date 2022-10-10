# print("====== DESAFIO 68 ======")

from random import  randint

vitorias = 0
resultado= ""

print("-="*20)
print("Vamos jogar Impar ou Par")
print("-="*20)
while True:
    computador = randint(0, 10)
    print("Faça sua jogada! ")
    numero = int(input("Digite um valor: "))
    escolha=" "
    while escolha not  in "IP":
        escolha = input("[I] Impar ou [P] par: ").strip().title()[0]


    if (numero+computador)%2 == 0:
        resultado = "Par"
        if escolha == "P":
            vitorias = vitorias+1
            print(f"\nParabéns! deu {resultado}")
            print("-=" * 20)
        else:
            break
    else:
        resultado = "Impar"
        if escolha == "I":
            vitorias = vitorias + 1
            print(f"\nParabéns! deu {resultado}\n")
            print("-=" * 20)
        else:
            break
    print("Mais uma vez..")

if vitorias >0:
    print(f"Você perdeu\n o computador jogou {computador} e você {numero} o {numero+computador} é {resultado}, você ganhou {vitorias} vezes")

else:
    print("GAME OVER! PERDEU DE PRIMEIRA")
print("Tente outra vez!")