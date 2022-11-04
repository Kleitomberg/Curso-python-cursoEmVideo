#DESAFIO 96
def calcularArea(l,c):
    area = l*c
    print("-="*20)
    print(f"A área de um terreno {l} x {c} é = {area}m²")

print("Controle de Terreno!")
print("-"*25)
largura = float(input("LARGURA EM m: "))
comprimento = float(input("Comprimento em m: "))

calcularArea(largura,comprimento)
