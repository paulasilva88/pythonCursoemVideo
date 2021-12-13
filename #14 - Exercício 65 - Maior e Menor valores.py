'''Crie um programa que leia vários números inteiros pelo teclado. No final
da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores'''

resposta = str(input('Digite \'s\' se quiser adicionar valores: '))
maior = 0
menor = 0
soma = 0
contador = 0
while resposta =='s':
    valor = int (input('Digite o valor: '))
    soma = soma + valor
    if valor > maior:
        maior = valor
    elif valor < menor and menor ==0 :
        menor = valor
    contador = contador +1
    resposta = str(input('Digite \'s\' se quiser adicionar valores: '))

print('''A média dos números adicionados é {}.
O maior valor digitado foi: {}
O menor valor digitado foi: {}'''.format(soma/contador, maior, menor))