#DESAFIO 90

aluno = {}

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Media de {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'

elif aluno['media']>=6 and aluno['media']<7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
'''
print(f"O nome do aluno é {aluno['nome']}")
print(f"A Média do aluno é {aluno['media']}")
print(f"Portando a situação do aluno é {aluno['situacao']}")
'''
print("-="*30)
for k,v in aluno.items():
    print(f"{k} do aluno é {v}")
