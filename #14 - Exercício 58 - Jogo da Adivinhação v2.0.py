'''Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer'''

#Importação de bibliotecas
from random import randint
from time import sleep

num_pc = randint(0,10)
num_jogador = int (input('Adivinhe um número entre 0 e 10: '))
while num_jogador >10 or num_jogador <0: # Validação de que o número inserido pelo usuário está no intervalo falado
    num_jogador = int(input('Adivinhe um número entre 0 e 10: '))
while num_jogador !=num_pc:
    num_jogador = int(input('Você errou! Tente novamente!\n Adivinhe um número entre 0 e 10: '))
    while 10 < num_jogador or num_jogador < 0:
        num_jogador = int(input('Eu disse entre 0 e 10: !'))
print("Você venceu! O número pensado pelo computador foi: {}".format(num_pc))