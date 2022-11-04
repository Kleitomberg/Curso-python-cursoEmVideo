"""#praticando aula 19

pessoas = []
pessoa = {
    "nome":"Kleitomberg",
    "idade": 23,
    "sexo": "M"
}

print(pessoa["idade"]) #pega um valor pela chave

print(pessoa.keys()) #mostra as chaves do dicionario
print(pessoa.values()) #mostra os valores dentro do dicionario
del pessoa["sexo"] #deletando um item
print("__"*20)
print(pessoa.items()) #mostra os items do dicionario chave e valor de cada

pessoa["peso"]=61.5 #adicionando um novo item ao dicionario
print("__"*20)

pessoas.append(pessoa) #adicionadno um dicionario dentro de uma lista
pessoas.append(pessoa) #adicionadno um dicionario dentro de uma lista
pessoas.append(pessoa) #adicionadno um dicionario dentro de uma lista

print(pessoas)
print("__"*20)

for i,dicionario in enumerate(pessoas):
    print(f"Pessoa {i+1} {dicionario['idade']}")

print("__"*20)
#iterndo chave e valor
for c,k in pessoa.items():
    print(f"{c} = {k}")

"""
estado = {}
brasil = []

for i in range(0,3):
    estado["uf"] = str(input("DIGITE UM ESTADO: "))
    estado["sigla"] = str(input("DIGITE UMA SIGLA: "))
    print(estado)
    brasil.append(estado.copy())

print(brasil)

for std in brasil:
    print(std["uf"])
