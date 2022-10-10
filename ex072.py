# print("====== DESAFIO 72 ======")

#tupla de numeros de 0 a 20 por extenso
numeros = (
    'zero', 'um', 'dois', 'Três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', '10',
    'onze', 'doze','treze','catorze','quinze','dezesseis','dezessete','dezoite','dezenove','vnte'
)


while True:

    meuNumero = int(input('Digite um numero de 0 a 20: '))

    if meuNumero <0 or meuNumero >20:
        print('Erro, por favor digite um valor valido')

    else:
        break




print(f"Você digitou o numero {numeros[meuNumero]}")


