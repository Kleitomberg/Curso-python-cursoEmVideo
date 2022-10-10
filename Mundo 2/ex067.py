# print("====== DESAFIO 67 ======")

while True:
    tabuada = int(input("Qual tabuada deseja ver: "))

    if tabuada < 0:
        break
    for i in range(1,11):
        print(f'{tabuada} X {i:2} = {tabuada*i}')

print("Acabou!")