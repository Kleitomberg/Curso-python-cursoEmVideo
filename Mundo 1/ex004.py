print("====== DESAFIO 04 ======")
algo = input('Digite algo aqui: ')


print('{} Isso que você digitou, É numero? {}, é um texto? {}, seu tipo é {}'.format(algo, algo.isnumeric(), algo.isalpha(), type(algo)))

if(algo.isnumeric()):
    print('{} É um numero'.format(algo))

if(algo.isupper()):
    print('{} É Maicuscula'.format(algo))

if(algo.islower()):
    print('{} É minuscula'.format(algo))

if(algo.isalpha()):
    print('{} É um texto'.format(algo))

if type(algo) == str:
    print('{} É um String'.format(algo))

if type(algo) == int:
    print('{} É um numero inteiro'.format(algo))

if type(algo) == bool:
    print('{} É um valor boleano'.format(algo))

if type(algo) == float:
    print('{} É um numero real'.format(algo))