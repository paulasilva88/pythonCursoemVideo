'''Faça um programa que leia uma frase pelo teclado e mostre
- Quantas vezes aparece a letra 'A';
- Em que posição ela aparece e primeira vez;
- Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip()
maiuscula = frase.upper()
qtd = maiuscula.count('A')
print('A frase digitada possui {} letras as'.format(qtd))
a= maiuscula.find('A')
print('A primeira vez em que ela aparece é na posição {}.'.format(a+1))
print('E a posição em que ela aparece pela última vez é {}.'.format(maiuscula.rfind('A')+1))
#Dá para usar o rfinder também
#Lembrar de colocar o +1 quando se falar em posição em listas ou strings

