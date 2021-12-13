'''
Crie um programa que leia vários números inteiros pelo teclado. O pro-
grama vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos núemros foram digitados e a soma entre eles
(desconsiderando o flag.) *
'''
contador = soma =0
numero = int(input('Digite um número: (Digite 999 para parar o programa) '))
while numero!= 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número: (Digite 999 para parar o programa) '))
print('Foram digitados {} números. A soma deles é {}.'.format(contador, soma))