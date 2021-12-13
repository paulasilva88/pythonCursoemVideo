'''Escreva um programa que leia um númro n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonacci.
'''

termo1 = 1
termo2 = 1
contador = 1
qtd = int(input('Quantos números da sequência de fibonacci você quer ver?'))
if qtd == 0:
    print('FIM DO PROGRAMA')
elif(qtd==1):
    print(termo1)
elif qtd>=2:
    print(termo1)
    while contador<qtd:
        print(termo2)
        reserva = termo2
        termo2 = termo2 + termo1
        termo1 = reserva
        contador += 1
