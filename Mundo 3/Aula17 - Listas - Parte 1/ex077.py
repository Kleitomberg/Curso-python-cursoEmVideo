
print("DESAFIO 77")

palavras =("casa","pedra","bola","papel","tesoura","livro")

for p in palavras:
    print(f"\nna plavra {p.upper()} são vogais:",end='')

    for letra in p:
        if (letra in 'aeiou'):
            print(f"{letra}",end=' ')





