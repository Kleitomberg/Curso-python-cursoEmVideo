print("====== DESAFIO 20 ======")

from random import sample
a1 = str( input('Nome do aluno 1'))
a2 = str( input('Nome do aluno 2'))
a3 = str( input('Nome do aluno 3'))
a4 = str( input('Nome do aluno 4'))

lista = [a1, a2, a3, a4]
escolhido = sample(lista, k=4)

print(escolhido)
