'''Crie um programa que leia vários núemros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre elas (desconsiderando o flag)'''

numero = soma = contador = 0
while True:
    numero = int (input('Digite um número: (999 para parar o programa) '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Foram digitados {contador} números. A soma deles é {soma}.')