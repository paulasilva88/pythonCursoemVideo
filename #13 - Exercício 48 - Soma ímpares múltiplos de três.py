'''Faça um programa que calcula a soma entre todos os
números ímpares que são múltiplis de três e que se encontram no
intervalo de 1 até 500'''
contador = 0
for i in range(3,500,6):
    contador = contador + i
print('A soma dos múltiplos de 3 contidos entre 3 e 500 é: {}'.format(contador))

#outra forma
cont = 0
for c in range(3,500, 3):
    if c%2==1:
        cont = cont +c
print('A soma dos múltiplos de 3 contidos entre 3 e 500 é: {}'.format(cont))