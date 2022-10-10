#print("====== DESAFIO 49 ======")

tabu = int(input('Ver tabuada de : ') )

print('_' * 13)

for i in range(1,11):
    print('{}  x {:2} = {}' .format(tabu, i,tabu*i))

print('_' * 13)