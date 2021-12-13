'''Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos'''

peso = float(input('Digite o peso da pessoa 1, em kg: '))
maior = peso
menor = peso
for i in range(4):
    peso = float(input('Digite o peso da pessoa {}, em kg: '.format(i+2)))
    if maior< peso:
        maior = peso
    if menor> peso:
        menor = peso
print('''Maior peso digitado: {}
Menor peso digitado: {}'''.format( maior, menor))
