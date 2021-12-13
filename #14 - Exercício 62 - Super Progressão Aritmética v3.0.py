'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar
0 termos.
'''
from typing import Any
primeiro_termo = float(input('Digite o primeiro termo da PA: '))
termo = primeiro_termo
razao  = float(input('Digite a razao da PA: '))
contador = 0
while contador<primeiro_termo+(razao*9):
    print(termo)
    termo = termo + razao
    contador = contador + razao

mais = str(input('Deseja mostrar mais um número da progressão? Se sim, digite \'s\': '))
while mais == 's':
    termo = termo + razao
    print(termo)
    mais = str(input('Deseja mostrar mais um número da progressão? Se sim, digite \'s\': '))
print('{}Fim do programa{}'.format ('-'*20, '-'*20))

    