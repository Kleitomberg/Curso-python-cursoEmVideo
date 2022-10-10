#desafio 83

exp = str(input("Digite uma expressão: "))

if exp.count("(") == exp.count(")"):
    print("Expressão OK")
else:
    print("Expressão invalida")



print("Resposta do video")

pabertos = []
exp = str(input("Digite uma expressão: "))

for c in exp:
    if c == "(":
        pabertos.append(c)
    elif c == ")":
        if len(pabertos) > 0:
            pabertos.pop()#remove um aberto
        else:
            pabertos.append(")")
            break

if len(pabertos) == 0:
    print("EXPRESSÃO É VALIDA")
else:
    print("Expressão invalida")

