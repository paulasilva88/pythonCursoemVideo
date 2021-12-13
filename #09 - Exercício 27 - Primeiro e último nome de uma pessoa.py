'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente'''
nome_completo = str(input('Digite seu nome completo: '))
lista = nome_completo.split()
print('Primeiro nome: {}'.format(lista[0]))
#print('ùltimo nome: {}'.format(lista[-1])) # Minha versão
print('Último nome: {}'.format(lista[len(lista)-1])) #Versão guanabara
