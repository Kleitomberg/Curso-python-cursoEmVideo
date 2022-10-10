#print("====== DESAFIO 63 ======")


fnn = int(input("Infome um numero: "))

t1 = int(0)
t2 = int(1)
c = 3

print("{} => {}".format(t1,t2),end=" => ")
while c <= fnn:
    t3 = t1 + t2
    print( t3, end=" => ")

    t1 = t2
    t2 = t3
    c+=1