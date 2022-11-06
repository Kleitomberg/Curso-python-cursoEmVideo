#DESAFIO 106
from time import sleep

cores = {
    'padrão':'\033[m',
    'cinza':'\033[0;30;47m',
    'azulBB':'\033[0;30;46m',
    'roxo':'\033[0;30;45m',
    'azul':'\033[0;30;44m',
    'amarelo':'\033[0;30;43m',
    'verde':'\033[0;30;42m',
    'vermelho':'\033[0;30;41m',
    'branco':'\033[0;40m'

}

def titulo(msg,cor):
    print(f"{cores[f'{cor}']}=" * (len(msg)+4))
    print(f"  {msg}")
    print(f"=" * (len(msg)+4))

def kabehelp(comando):

    titulo(f'Acessando Manual do comando {comando}','amarelo')
    sleep(0.5)
    print(cores['azul'])
    return help(comando.lower())

while True:

    titulo("SISTEMA DE AJUDA KABEHELP",'verde')
    print('\033[m')
    comando = str(input("Comando ou Biblioteca > "))
    print()
    if comando.upper() == 'FIM':
        titulo("ATÉ LOGO",'vermelho')
        break
    else:
        kabehelp(comando)
        sleep(1)
