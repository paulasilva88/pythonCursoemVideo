'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
total = qtd_1000 = 0
decisao = ' '
while True:
    print('-'*60)
    print ('Digite as informações sobre o produto!')
    nome = str(input('Nome: ')).strip().upper()
    preco = float(input('Preço: R$'))
    # Preço total
    total = total + preco
    print('-' * 60)
    # Mais caros que 1000
    if preco >1000 :
        qtd_1000 +=1
    if decisao not in 'SN':
        menor = preco
        nome_barato = nome
    if menor>preco:
        nome_barato = nome
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Deseja adicionar mais produtos? [S/N] ')).strip().upper()
    if decisao == 'N':
        break
print('-'*60)
print(f'O valor total gasto foi de R${total:.2f}')
print(f'Há {qtd_1000} produtos que custam mais de R$1000.')
print(f'O produto mais barato é: {nome_barato}')


