print("====== DESAFIO 11 ======")

altura = float(input('Digite a Altura: '))
largura = float(input('Digite a Largura: '))
area = altura*largura

quantidadeDeTinta = area/2

print('Uma parede de {}m² precisa de {} litros de tinta para pintura' .format(area, quantidadeDeTinta))