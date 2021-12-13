'''Crie um programa que leia uma frase qualquer e diga se ela é palídromo,
desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).strip()
lista= frase.split(' ')
frase_sem_espacos =''.join(lista)
palindromo = True
for i in range(len(frase_sem_espacos)):
    if frase_sem_espacos[i]!=frase_sem_espacos[len(frase_sem_espacos)-i-1]:
        palindromo = False
        break
print(' A frase \'{}\' é um palíndromo'.format(frase) if palindromo ==True else 'A frase \'{}\' não é um palíndromo'.format(frase))

