#desafio 80

numeros = []

for i in range(0,5):

    print(numeros)
    valor = int(input(f"Digite um valor: "))
    if i == 0:
        print("primeiro valor adicionado a lista...")
        numeros.insert(0,valor)
    else:
        if valor > numeros[len(numeros)-1]:
            print("Adicional ao final da lista")
            numeros.append(valor)

        elif valor < numeros[len(numeros)-1] and valor > numeros[len(numeros)-2]:
            print(f"adicionado na posição {len(numeros)-1}")
            numeros.insert(len(numeros)-1,valor)

        elif valor < numeros[0]:
            print("Adicionado no inicio da lista")
            numeros.insert(0,valor)
        elif valor > numeros[0] and valor < numeros[1]:
            print("Adicionado na posição 1 aa")
            numeros.insert(1, valor)

       # print("Valor inserido na posição ", end='')

    for v in numeros:
        if v > valor:
            pass
          # print(f"{numeros.index(v)-1}")

print(numeros)


