print("====== DESAFIO 23 ======")

valor = int( input('Digite um numero entre 0 e 9999: '))

milhar = (valor//1000) % 10
centena = (valor//100) % 10
dezena = (valor//10) % 10
unidade = (valor//1) % 10

print('Milhar = {}' .format(milhar))
print('Centena = {}'.format(centena))
print('Dezena = {}' .format(dezena))
print('Unidade = {}' .format(unidade))