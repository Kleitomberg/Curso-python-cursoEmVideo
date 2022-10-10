# print("====== DESAFIO 73 ======")

classificação = (
    'Corinthians', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba','Avaí',
    'América-MG','Palmeiras','Bragantino','Internacional','Fluminense','Goiás', 'Cuiabá',
    'Athletico-PR','Flamengo','Juventude','Ceará','Atlético-GO','Fortaleza'
)

print('A\n')
print(f' Os 5 Primeiros colocados do Brasileirão são \n {classificação[0:5]} \n')

print('B')
print(f'Os 4 ultiumos colocados são {classificação[16:]}')

print('C\n')
print(f" Todos os time em ordem alfabetica {sorted(classificação)}")

print('D\n')
print(f" O Flamengo encontra-se na posição {classificação.index('Flamengo')+1}º")
