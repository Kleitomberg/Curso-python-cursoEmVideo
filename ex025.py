print("====== DESAFIO 25 ======")

nome = input('Digite um nome: ').strip().title()

tem = nome.find('Silva')


print('Tem silva ? {}' .format( nome[nome.find('Silva'):nome.find('Silva')+5] =='Silva' ))

if tem == -1:
    print('Não Tem Silva no nome')
else:
    print('Tem Silva no nome')