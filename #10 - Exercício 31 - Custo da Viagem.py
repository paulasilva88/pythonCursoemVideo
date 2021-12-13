'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até
200km e R$0,45 para viagens mais longas. '''

distance = float(input('Qual a distância entre seu destino e a sua origem, em km? '))

print('O valor da sua passagem é R${:.2f}!'.format(distance*0.50) if distance<=200 else 'O valor da sua passagem é R${:.2f}'.format(distance*0.45))
