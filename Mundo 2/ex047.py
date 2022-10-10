# print("====== DESAFIO 47 ======")

pares = []
cp = 0
for p in range(1,51):
    if p%2==0:
        cp = cp + 1
        #pares.append(p)
        print("{}".format(p), end=" ")

#print("Entre 1 e 50 há {} pares,\n que são {}".format(cp, pares))