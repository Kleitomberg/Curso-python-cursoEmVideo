print("====== DESAFIO 17 ======")

from math import hypot
catetoOposto = float(input('Cateto Oposto: '))
catetoAdjacente = float(input('Cateto Adjacente: '))

hipotenusa = hypot(catetoOposto,catetoAdjacente)

print('hipotenusa vale {:.2f}'.format(hipotenusa))
