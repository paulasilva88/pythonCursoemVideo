'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

 - Média abaixo de 5.0:
 REPROVADO

 - Média entre 5.0 e 6.9:
 RECUPERAÇÂO
 - Média 7.0 ou superior:
 APROVADO'''

n1= float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media<5:
    print('Média: {}\n\033[31mSituação: REPROVADO!'.format(media))
elif media>=5 and media<7:
    print('Média: {}\n\033[34mSituação: RECUPERAÇÃO'.format(media))
else:
    print('Média: {}\n\033[32mSituação: APROVADO'. format(media))