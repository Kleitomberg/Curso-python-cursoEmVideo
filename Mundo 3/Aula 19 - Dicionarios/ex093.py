#DESAFIO 93

jogador = {}
gols = []


jogador['nome'] = str(input("Nome do Jogador: "))
quantidade_partidas = int(input(f"Partidas jogadas por {jogador['nome']}: "))

for i in range(0,quantidade_partidas):
    gols.append(int(input(f"Gols marcados na partida {i+1}: ")))

jogador['gols'] = gols[:]

jogador['total'] = sum(gols)
print("-="*30)
print(jogador)
print("-="*30)

for k,v in jogador.items():
    print(f"{k} = {v}")
print("-="*30)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas na carreira")
for pos,i in enumerate(jogador['gols']):
    print(f" => Na partida {pos+1} fez {i} gols.")
print(f" Fazendo assim um total de {jogador['total']} gols na carreira")

