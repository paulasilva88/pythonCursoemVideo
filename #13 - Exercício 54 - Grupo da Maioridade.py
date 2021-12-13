'''Crie um programa que leia o nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date
atual= date.today().year
maiores = 0
menores = 0
for i in range(7):
    idade = atual - int (input('Ano de nascimento da pessoa {}: '.format(i+1)))
    if idade>=21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('''Quantidade de maiores: {}
Quantidade de menores: {}.'''. format(maiores, menores))