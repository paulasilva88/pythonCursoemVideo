'''Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário. O programa
 será interrompedo quando o núemro solicitado fro negativo.
'''

print('-'*80)
print(f"{'PROGRAMA DE TABUADA':-^80}") #fstring, com determinação de ocupação de 80 espaços, espaços vazios preenchidos pelo '-' e centralizado '^'
while True:
    valor = int(input('De qual valor você quer saber a tabuada? (Digite um valor negativo para parar) '))
    if valor<0:
        break
    print(f"{'-':-^80}")
    for i in range (1,11):
        print(f'{valor} x {i:>2} = {valor *i}')
    print(f"{'-':-^80}")

print(f"{'FIM DO PROGRAMA':-^80}")
