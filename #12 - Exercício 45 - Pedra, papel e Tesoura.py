'''
Crie um programa qwue faça o computador jogar Jokenpô com voce
'''
from random import randint
pc = randint(1,3)
print('Bem vindo ao jo-ken-pô\n', '-'*100)
user = int(input('''Digite um número para escolher entre pedra, papel ou tesoura:
    1 - Pedra
    2 - Papel
    3 - Tesoura
    Sua escolha: '''))
print ('Escolha do pc: {}'.format(pc))

if pc ==1:
    if user ==1:
        print('Deu empate!')
    elif user == 2:
        print('Você venceu!')
    else:
        print('Você perdeu!:C')
elif pc == 2:
    if user == 1:
        print('Você perdeu!')
    elif user == 2:
        print('Deu empate!')
    else:
        print('Você ganhou!:C')
elif pc == 3:
    if user == 1:
        print('Você venceu!')
    elif user == 2:
        print('Você perdeu!')
    else:
        print('Deu empate!:C')

