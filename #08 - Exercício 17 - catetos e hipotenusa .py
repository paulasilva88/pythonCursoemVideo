'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''
from math import sqrt, hypot

catoposto = float(input('Digite o comprimento do cateto oposto: '))
catadjacente = float(input('Digite o comprimento do cateto adjacente: '))
#hipotenusa = sqrt(catoposto**2 + catadjacente**2)
hipotenusa = hypot(catoposto, catadjacente)
print ('A hipotenusa do triângulo retângulo é igual a {:.2f}'. format(hipotenusa))