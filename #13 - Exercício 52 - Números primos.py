'''Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo'''
valor = int(input('Digite um número qualquer: '))
primo = True
for i in range(valor-1, 1, -1):
    if valor%i ==0:
        primo = False
        break
print('O número {} é primo'.format(valor) if primo==True else 'O número {} não é primo'. format(valor))