#Desafio 92
from datetime import date
pessoa = {}

pessoa["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento"))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input("Carteira de trabalho (0 = Não tenho): "))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("Salário: "))
    idade_contratacao = pessoa['contratacao'] - nascimento #Quantos Anos Tinha Na Contratação
    pessoa['aposentadoria'] = idade_contratacao + 35

print("-="*20)
print("     PESSOA CADASTRADA    ")
print("-="*20)

for k,v in pessoa.items():
    if k == 'ctps' and  v == 0:
        print(f"{k} = Não possui Carteira")
    else:
        print(f"{k} = {v}")
