'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugada.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km rodado.'''

km = float(input('Quantos km foram rodados? '))
dias = int(input('Quantos dias de aluguel? '))
valor = (0.15*km) + (60* dias)
print ('O valor a ser pago por {} dias de aluguel e {}km rodados é R${:.2f}'. format(dias, km, valor))