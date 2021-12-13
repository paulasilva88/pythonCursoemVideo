'''Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.'''

from math import floor

num = float(input('Digite um número real qualquer: '))
print ('A parte inteira do número {} é {}'.format(num, floor(num)))

#Tem a função trunc também
#Dá para fazer pelo int
