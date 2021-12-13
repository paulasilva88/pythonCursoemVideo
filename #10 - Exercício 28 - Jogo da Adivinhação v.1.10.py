'''Escreva um programa que faça o computador 'pensar'  em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador

O programa deverpa escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep #Sugestão Guanabara
computer_number = randint(0,5) # Escolha de um número pelo computador

print('Vamos ver se você consegue adivinhar o mesmo número que o computador!' )
user_number = int(input('Type a number between 0 and 5: ')) #Escolha de um número pelo usuário
while user_number>5 or user_number<0:
    user_number = int(input('Type a number between 0 and 5: '))
print('PROCESSING...') #Sugestão Guanabara
sleep(3) #Faz o programa esperar 3 segundos para mostrar o resultado
print('You Win!' if user_number == computer_number  else 'Sorry, the Computer choose another number! :C')
print('PC number: {}'.format(computer_number))
print('Your number: {}'.format(user_number))

