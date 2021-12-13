'''Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais;
- Escaleno: todos os lados iguais'''


r1 = float(input('Digite um comprimento da primeira reta: '))
r2 = float(input('Digite um comprimento da segunda reta: '))
r3 = float(input('Digite um comprimento da terceira reta: '))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    if r1==r2==r3:
        print('As retas foram um triângulo equilátero.')
    elif r1==r2 or r2==r3 or r1==r3:
        print('As retas podem formar um triângulo isósceles')
    else:
        print('As retas podem formar um triângulo escaleno')
else:
    print('As retas não podem formar um triângulo')

