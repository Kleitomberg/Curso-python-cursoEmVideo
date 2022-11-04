#DESAFIO 99

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
    print(f"Foram informados {len(numeros)} valores!")
    print(numeros)
    print(f"O MAIOR NUMERO FOI {m}")
    print("-="*30)


maior(2,9,4,5,7,1)

maior(4,7,0)
maior(1,2)
maior(6)
maior()
