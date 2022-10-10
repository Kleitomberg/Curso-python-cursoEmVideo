print("====== DESAFIO 24 ======")

cidade = input('Digite o nome de uma cidade: ').strip()

separado = cidade.split()

primeiroNome = separado[0].title()


print('Santo' in primeiroNome)

if primeiroNome.find('Santo') == 0:
    print('A cidade {} começa com Santo'.format(cidade))
else:
    print('A cidade {} não começa com Santo'.format(cidade))