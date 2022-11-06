#DESAFIO 101

def vota(nascimento):
    from datetime import date
    ano_tual = date.today().year
    idade = ano_tual - nascimento

    if idade >=18 and idade<65:
        return f'Com {idade} anos: VOTO É OBRIGATÓRIO!'
    elif idade>=16 or idade>65:
        return f"Com {idade} anos: VOTO É OPCIONAL!"
    else:
        return f"Com {idade} anos: NÃO VOTA!"
print("-"*30)

nascimento = int(input("Em que ano você nasceu?: "))

print(vota(nascimento))
