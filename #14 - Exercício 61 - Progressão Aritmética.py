'''Refaça o desafio 51, lendo a razão de uma PA, mostrando os 10
primeiros termos da Progressão usando a estrutura while
'''

primeiro_termo = float(input('Digite o primeiro termo da PA: '))
termo = primeiro_termo
razao  = float(input('Digite a razao da PA: '))
contador = 0
while contador<primeiro_termo+(razao*9):
    print(termo)
    termo = termo + razao
    contador = contador + razao
    