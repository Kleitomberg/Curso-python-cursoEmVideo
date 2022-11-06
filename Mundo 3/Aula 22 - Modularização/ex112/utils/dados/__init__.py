def leiaDinheiro(msg):
    while True:
        valor = str(input(f'{msg}')).replace(",",".")
        if valor.isalpha() or valor.strip() == '':
            print(f"\033[1;31mErro! Porfavor informe um valor numerico.\033[m")
        else:
            valor = float(valor)
            break


    return valor
