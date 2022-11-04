#DESAFIO 95

time = []
jogador = {}
gols = []

while True:
    jogador['nome'] = str(input("Nome do Jogador: "))
    quantidade_partidas = int(input(f"Partidas jogadas por {jogador['nome']}: "))

    for i in range(0,quantidade_partidas):
        gols.append(int(input(f"Gols marcados na partida {i+1}: ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    print("-="*30)

    for k,v in jogador.items():
        print(f"{k} = {v}")
    print("-="*30)

    print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas na carreira")
    for pos,i in enumerate(jogador['gols']):
        print(f" => Na partida {pos+1} fez {i} gols.")
    print(f" Fazendo assim um total de {jogador['total']} gols na carreira")
    print()

    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        resp = str(input("Quer continuar? [S/N]: ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! DIGITE APENAS S OU N! ")

    if resp in 'Nn':
        break

print("-="*40)
print(time)
print("-="*40)

for i,jogador in enumerate(time):
    print(f"{i} Jogador = {jogador['nome']} - Gols = {jogador['gols']} - TOTAL = {jogador['total']}")

print("-="*20)
while True:
    print("__"*40)

    jog = int(input("Mostrar dados de  qual jogadoor? (999 = parar): "))
    if jog == 999:
        break
    if jog >= len(time):
        print("Jogador Não existe na lista!")
    else:
        print(f"-- Dados do jogador {time[jog]['nome']}")

        for i,gols in enumerate(time[jog]['gols']):
            print(f"Na partida {i+1} Marcou {gols} gols")


