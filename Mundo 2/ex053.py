#print("====== DESAFIO 53 ======")

from unidecode import unidecode

frase = input("Digite uma frase: ").upper().strip()

separado = frase.split(" ")
junto = "".join(separado)
semacento = unidecode(junto)
inv =""
tamanho = len(junto)

for i in range(tamanho-1,-1, -1):
    inv = inv+semacento[i]

print("A frase '{}' invertida é '{}' ".format(semacento, inv))

if semacento == inv:
    print("É um Palindromo")

else:
    print("NÃO é Palindromo")