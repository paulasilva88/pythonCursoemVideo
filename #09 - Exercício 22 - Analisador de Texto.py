'''Crie um programa que leia o nome completo de uma pessoas e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo (sem considerar os espaços);
- Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip() #O strip foi sugestão do prof Guanabara
print('Nome em maiúsculo: {}.'.format(nome.upper()))
print('Nome em minúsculo: {}.'.format(nome.lower()))
lista = nome.split(' ')
nome_junto = ''.join(lista)
#print('O seu nome completo tem {} letras.'.format(len(nome_junto))) # Minha versão
print('O seu nome completo tem {} letras.'.format(len(nome) - nome.count(' '))) # quantidade de letras da string menos a quantidade de espaços
#print('O primeiro nome possui {} letras'.format(len(lista[0]))) # Minha versão
print ('O primeiro nome tem {} letras.'.format(nome.find(' '))) #A primeira palavra termina no primeiro espaço

