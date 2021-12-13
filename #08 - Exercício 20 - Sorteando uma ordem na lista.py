''' O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import choice, shuffle
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
'''escolhido = choice(lista)
print('A ordem de apresentações será: \n1º {}'.format(escolhido))
lista.remove(escolhido)
escolhido = choice(lista)
print('2º {}'.format(escolhido))
lista.remove(escolhido)
escolhido = choice(lista)
print('3º {}'.format(escolhido))
lista.remove(escolhido)
escolhido = choice(lista)
print('4º {}'.format(escolhido))'''

#usando Shuffle
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

