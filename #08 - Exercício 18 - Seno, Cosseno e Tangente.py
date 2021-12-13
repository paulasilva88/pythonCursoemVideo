'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo em graus: '))
angulo = radians(angulo)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print ('O seno, o cosseno do ângulo {:.2f} rad são: \nSen: {:.2f};\nCos: {:.2f} ; e \nTan: {:.2f}.'.format(angulo, seno, cosseno, tangente))

