'''
Faça um programa qe leia três número e mostre qual é o maior e qual é
o menor
'''
number1 = float(input('Digite um número: '))
menor = number1
maior = number1
number2 = float(input('Digite outro número: '))
if number1>=number2:
    menor = number2
else:
    maior = number2
number3 = float(input('Digite mais um número: '))
if number3<=menor:
    menor = number3
print('O menor número digitado foi: {}'.format(menor))
if number3>maior:
    maior = number3
print('O maior número digitado foi: {}'.format(maior))

