print("====== DESAFIO 18 ======")


from math import sin, tan, cos, radians
angulo = float(input('Informe um Angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O Seno de {} é {:.2f}'.format(angulo, seno))
print('O Cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A Tangente de {} é {:.2f}'.format(angulo, tangente))