print("DESAFIO 76")
print("\n")
produtos = ("notebook",3000,
            "computador",5000,
            "teclado",300,
            "mouse",230,
            "monitor",2000)

print("_____________LISTAGEM DE PREÇO___________________")
for p in range(0,len(produtos),2):

    print(f'{produtos[p].title()}......................R$ {produtos[p + 1]}')

print("____________________________________________________")

print("")
print("-="*20)
print("RESPOSTA DO VIDEO: ")


listagem = (
    "Lápis",1.75,
    "Borracha",2,
    "Caderno",15.90,
    "Estojo",25,
    "Transferidor",4.20,
    "Compasso",9.99,
    "Mochila",120.32,
    "Canetas",22.30,
    "Livro",34.90
)
print("\n")
print("-"*30)
print("Listagem de Preços")
print("-"*30)
for pos in range(0, len(listagem)):
    if pos%2==0:
        print(f"{listagem[pos]:.<15}",end='')
    else:
        print(f"R${listagem[pos]:>7.2f}")

