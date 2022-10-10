print("====== DESAFIO 09 ======")

tabu = int(input('Ver tabuada de : ') )
''' 
print('{} x 1 = {}' .format(tabu, tabu*1))
print('{} x 1 = {}' .format(tabu, tabu*2))
print('{} x 1 = {}' .format(tabu, tabu*3))
print('{} x 1 = {}' .format(tabu, tabu*4))
print('{} x 1 = {}' .format(tabu, tabu*5))
print('{} x 1 = {}' .format(tabu, tabu*6))
print('{} x 1 = {}' .format(tabu, tabu*7))
print('{} x 1 = {}' .format(tabu, tabu*8))
print('{} x 1 = {}' .format(tabu, tabu*9))
print('{} x 1 = {}' .format(tabu, tabu*10))
'''
i=1

print('_' * 13)
while i<=10:
    print('{} x {:2} = {}' .format(tabu, i,tabu*i))
    i += 1
print('_' * 13)