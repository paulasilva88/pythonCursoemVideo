'''Faça um programa que leia um núemro qualquer e mostre seu fatorial
'''
'''
numero = int(input('Digite um número que você quer saber o fatorial: '))
fatorial = 1
mult = 2
while mult<=numero:
    fatorial = fatorial* mult
    mult = mult + 1
print('O fatorial do número {} é {}'. format(numero, fatorial))'''

#versão com o for:
numero = int(input('Digite um número que você quer saber o fatorial: '))
fatorial = 1
for i in range(numero):
    fatorial = fatorial * (i+1)
print('O fatorial do número {} é {}'. format(numero, fatorial))