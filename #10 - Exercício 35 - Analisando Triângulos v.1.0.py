'''Desenvolva um programa que leia o comprimento de retas e diga aos
usuário se elas podem ou não formar um triângulo'''

r1 = float(input('Digite um comprimento da primeira reta: '))
r2 = float(input('Digite um comprimento da segunda reta: '))
r3 = float(input('Digite um comprimento da terceira reta: '))
print('As retas podem formar um triângulo!' if r1+r2>r3 and r2+r3>r1 and r1+r3>r2 else 'As retas não podem formar um triângulo')
