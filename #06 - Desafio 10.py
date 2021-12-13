'''Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
considerando que US$1,00 = R$3,27'''

r= float (input('Quantos reais você tem? '))
print('Com RS{:.2f} você pode comprar US${:.2f}!'.format(r, r/3.27))