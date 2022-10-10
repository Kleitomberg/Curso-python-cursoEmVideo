#print("====== DESAFIO 60 ======")
print("Calcule o fatorial! ")

numero = int(input("Infome um numero: "))
i = numero
fa=1
f=0

while i > 0:
    print(i,end="")
    print(end=" X " if i > 1 else " = {}".format(fa))
    fa =fa*i
    '''
    if i == numero:
        f = f + (i *(numero-1))

    elif i > 1:
        if i != 0:
            f = f *(i-1)
'''
    i-=1

print("\nFim {}".format(i))

#print("\no fatorial de {}! é {}".format(numero,f))