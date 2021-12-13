'''Crie um programa que leia dois valores e mostre um meno na tela:

[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

'''
#Entrada de valores
n1=  float(input(  'Digite um número: '))
n2 = float(input('Digite outro número: '))
menu = (int(input('''Digite o número correspondente ao que você deseja fazer com os números digitados:
[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa\n Digite aqui: ''')))
print('-'*55)
while menu !=5:
    if menu == 1:
        print('A SOMA dos números digitados é: {}.'. format(n1+n2))
        break
    elif (menu ==2):
        print('O PRODUTO dos números adicionados é: {}'.format(n1*n2))
        break
    elif menu ==3:
        print('Entre os números digitados o maior é o {}'. format(n1) if n1>=n2 else 'Entre os números digitados, o maior é {}'.format(n2))
        break
    elif menu ==4:
        n3 = float(input('Digite outro número: '))
        menu = (int(input('''Digite o número correspondente ao que você deseja fazer com os números digitados:
        [1] Somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa\n Digite aqui: ''')))
        print('-' * 55)
print('{}Fim do programa{}'. format('-'*20, '-'*20))