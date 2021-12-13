'''Faça um programa que jogue par ou ímpar com o computador,
O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que eel conquistou no final do jogo.'''
from random import randint
contador =0
while True:
    valor = int(input('Digite um número: '))
    aposta = str(input('Você aposta em par ou ímpar? [P ou I] ')).upper().strip()
    pc = randint(1,11)
    soma = valor + pc

    if soma%2 == 0:
        paridade = 'P'
        print(f'Você digitou {valor} e o computador digitou {pc}, a some deu {soma}, PAR!')
    else:
        paridade = 'I'
        print(f'Você digitou {valor} e o computador digitou {pc}, a some deu {soma}, ÍMPAR!')
    if paridade != aposta:
        print(f'Você perdeu! Mas consegui vencer {contador} vezes')
        break
    else:
        contador +=1
