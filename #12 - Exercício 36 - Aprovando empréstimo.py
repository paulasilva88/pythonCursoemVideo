'''Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da
casa, o slário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado'''

print('\033[31molá, mundo\033[m')
print('''Bem vindo(a) ao sistema de financiamento de casas do Banco XX!!
{}'''.format('-'*70))
#Entrada de informações do usuário
valor = float(input('Qual o valor da casa que você deseja financiar? R$'))
salario = float(input('Qual o seu salário ou renda mensal? R$'))
anos = int(input('Em quantos anos você deseja pagar pela casa? '))
#Cálculo da prestação
prestacao = valor/(12*anos)
#Cálculo compatibilidade prestação e salário
print('Valor mensal a ser pago: ',prestacao)
print('30% do seu salário: ', salario*0.3)
print('\033[32mEmpréstimo aprovado!\033[m' if salario*0.3>=prestacao else '\033[31mEmpréstimo negado, sentimos muito!\033[m')