'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

lista = [0,0,0,0]
notas = [50,20,10,1]
contador = 0
print ('-'*60)
print('{:^60}'.format(' BANCO PYTHON '))
print ('-'*60)
valor_saque = int(input('Quanto você deseja sacar? R$'))
print ('-'*60)
print(f'Para sacar o valor de {valor_saque} serão utilizadas:')
while valor_saque > 0:
    for i in range(4):
        lista[contador] = valor_saque//(notas[i])
        valor_saque = valor_saque%(notas[i])
        contador += 1
        if lista[i] > 0:
            print(f'{lista[i]} notas de R${notas[i]};')
print('{:-^60}'.format(' FIM DO PROGRAMA '))
