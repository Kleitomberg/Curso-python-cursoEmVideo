print("====== DESAFIO 26 ======")

frase = input("Digite uma frase: ").strip().upper()

print('A frase "{}" possui {} letras A'.format(frase, frase.count('A')))

print('A primeira letra A encontra-se na posição {}'.format(frase.find('A')+1))

print('A Ultima letra A encontra-se na posição {}'.format(frase.rfind('A')+1 ))