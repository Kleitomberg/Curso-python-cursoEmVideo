#DESAFIO 99
from time import sleep
def maior(*numeros):
    m = 0
    for i,n in enumerate(numeros):
        if i ==0:
            m = n
        else:
            if n > m:
                m = n
    print("-=" * 30)
    print("Analizando valores...")
    for n in numeros:
        sleep(0.5)
        print(f"{n} ", end='')
    print(f"| Foram informados {len(numeros)} valores!")
    print(f"O MAIOR NUMERO FOI {m}")

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
