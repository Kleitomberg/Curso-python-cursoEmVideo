#Desafio 103

def ficha(nome="<desconhecido>",gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato")

print("-"*30)

jogador = str(input("Nome do Jogador: "))
while True:
    golsMarcados = str(input("Gols Marcados: "))

    if golsMarcados.isnumeric() or golsMarcados == "":
        break
    else:
        print("Erro por favor informe um numero válido!")


if jogador == '' and golsMarcados == '':
    ficha()

elif jogador == '':
    ficha(gols = golsMarcados)

elif golsMarcados == '' or not golsMarcados.isnumeric():
    ficha(nome=jogador)


else:
    ficha(jogador,golsMarcados)
