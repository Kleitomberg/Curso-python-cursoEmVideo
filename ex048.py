# print("====== DESAFIO 48 ======")
imapres = []
multiplo = 0
soma = 0
for i in range(1,501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma+i
        multiplo = multiplo+1

print("A soma dos {} impares multiplos de 3 entre 1 e 500 é {}".format(multiplo,soma))