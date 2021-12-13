'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher entre qual a base será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

valor = int(input('Digite um número real: '))
binario = bin(int(valor))
octal = oct(valor)
hexadecimal = hex(valor)
print('''O valor {} em outras bases:
Binário: {}
Octal: {}
Hexadecimal: {}'''.format(valor,binario[2:], octal[2:], hexadecimal[2:]))
