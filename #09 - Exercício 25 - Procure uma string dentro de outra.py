'''Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome'''
nome = str(input('Digite seu nome completo: ')).strip()
maiusculo = nome.upper()
if 'SILVA' in maiusculo:
    print('No seu nome tem Silva')
else:
    print('No seu nome não tem Silva')