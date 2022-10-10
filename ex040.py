print("====== DESAFIO 40 ======")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n2+n1)/2

if media < 5:
    print("\033[1:31mReprovado\033[m Sua média foi \033[1:33m{:.1f}\033[m".format(media))
elif media >= 5 and media < 7:
    print("\033[1:33mRecuperação!\033[m Sua media foi {:.1f}" .format(media))
elif media>= 7:
    print("\033[1:32mAprovado!\033[m \033[1:34mMedia = {:.1f}\033[m".format(media))