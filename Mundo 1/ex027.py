print("====== DESAFIO 26 ======")

nomeCompleto = input('Digite seu nome completo: ').strip().title()

separado = nomeCompleto.split()
x=len(separado)
primeiroNome = separado[0].title()
ultimoNome = separado[x-1].title()

print('Seu nome é {}'.format(nomeCompleto))
print('Primeiro nome é {}'.format(primeiroNome))
print("Ultimo Nome é {}".format(ultimoNome))