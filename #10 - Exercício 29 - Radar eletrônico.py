'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''
import colorsys
v = float(input('Qual a velocidade do carro, em km/h? '))
print('Velocidade Digitada: {}'. format(v) if v<=80 else 'Você ultrapassou 80km/h, deverá pagar uma multa de R${.2f}'.format((v-80)*7))
#Lembrar de formatar valores em dinheiro: R$ + {.2f}
