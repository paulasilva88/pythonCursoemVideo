'''Faça um programa que leia o nome de uma cidade e diga se ela 
começa ou não com 'SANtos'''
cidade = str(input('Digite o nome da cidade: ')).upper()
cidade = cidade.lstrip()
if 'SANTO' in cidade[:5]:
    print('O nome da cidade se inicia com Santo')
else:
    print('O nome da cidade não se inicia com Santo')