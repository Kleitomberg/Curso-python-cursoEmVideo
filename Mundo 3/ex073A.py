#print("DESAFIO 073")

serieA = (
    "Palmeiras","Internacional","Fluminense","Corinthians","Flamengo","Athletico-PR","Atlético-MG","América-MG",
    "Fortaleza","Botafogo","Santos","Goiás","São Paulo","Bragantino","Coritiba","Ceará","Cuiabá","Avaí","Atlético-GO",
    "Juventude"
)
print("-="*20)
print("TABELA COMPLETA")
for pos,time in enumerate(serieA):
    print(f"{pos+1} - {time}")

print("-="*20)
print("\n5 PRIMEIRO SÃO: \n")
print(serieA[0:5])
print("")
for time in range(0,5):
    print(f" {time+1} - {serieA[time]}")

print("-="*20)
print("\n ZONA DO REBAIXAMENTO: \n")
print(serieA[-4:])
print("")
for time in range(len(serieA)-4,len(serieA)):

    print(f"{time+1} - {serieA[time]}")
    #print(f" {time+1} - {serieA[time]}")

print("-="*20)
print("\n ORDEM ALFABETICA \n")

print(sorted(serieA))

print("-="*20)
print("\n EM QUE POSIÇÃO ESTA O GOIAS \n")

print(f' O GOIÁS ENCONTRA-SE NA {serieA.index("Goiás")+1}° POSIÇÃO')
print("-="*20)
