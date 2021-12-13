'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule:
a sua área e
a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².'''
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
area = l*h
print('A área da parede {} x {}  é igual a {} e será preciso {:.2f} litros de tinta'.format(l, h, area, area/2))