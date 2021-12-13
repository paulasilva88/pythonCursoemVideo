'''Faça um programa que leia um número de 0 a 9999 e mostre
na tela um dos dígitos separados'''


numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero%10
dezena = numero//10%10
centena = numero//100%10
milhar =numero//1000%10

print('Unidade: {}'. format(unidade))
print('Dezena: {}'. format(dezena))
print('Centena: {}'. format(centena))
print('Milhar: {}'. format(milhar))


''' - Minha implementação - usando strings
valor = str(input('Digite um número entre 0 e 9999: '))
while int(valor) > 9999 or int(valor)<0:
    valor = str(input('Digite um número entre 0 e 9999: '))
if len(valor) ==1:
    print('Unidade: {}'.format(valor))
elif   len(valor) ==2:
    print('Unidade: {}\nDezena: {}.'.format(valor[1], valor[0]))
elif   len(valor) ==3:
    print('Unidade: {}\nDezena: {}\nCentena: {}.'.format(valor[2], valor[1], valor[0]))
else:
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(valor[3], valor[2], valor[1], valor[0] ))

'''