print("====== DESAFIO 15 ======")

dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodados nesses dis? '))

valorParaPagar = ( (dias*60)+(km*0.15) )

print('Deve ser pago {:.2f}R$'.format(valorParaPagar))
