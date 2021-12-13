'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
from datetime import date #importação de biblioteca de tempo


year = int(input('Digite o ano, e se quiser o ano atual, digite 0: '))
if year ==0:
    year = date.today().year
print('O ano de {} é bisgggsexto!'.format(year) if year % 4 ==0 and year %100 !=0 or year %400 ==0 else 'O ano de {} NÂO é bissexto'.format(year))

#Anos bissextos não são determinados apenas por serem múltiplos de 4, também não podem ser múltimos de