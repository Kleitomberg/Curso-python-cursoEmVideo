print("====== DESAFIO 22 ======")

texto = input('Digite seu nome completo: ').strip()

primeiroespaco = texto.find(' ')
junto = "".join(texto.split())

print(texto.upper())
print(texto.lower())
print('total de letras sem espaços é {}'.format(len(junto)))
print('Seu primeiro nome é {} '.format(texto[:primeiroespaco]))
print('O primeiro nome possui {} letras'.format(len(texto[:primeiroespaco])))
