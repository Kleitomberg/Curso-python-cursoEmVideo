
list1 = []
pessoas =[]
maior = menor = 0
for i in range(0,3):
    list1.append(str(input("Digite um nome: ")))
    list1.append(int(input("Digite a idade: ")))
    pessoas.append(list1[:])
    list1.clear()


print(pessoas)

for p in pessoas:
    if p[1]>18:
        maior+=1
    else:
        menor+=1

print(f"Ao total temos {maior} pessoas mmaiores e {menor} pessoas menores de idade")
