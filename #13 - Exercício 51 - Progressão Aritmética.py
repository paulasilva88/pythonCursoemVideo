'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

'''
primeiro_termo = int(input('Digite o primeiro dígito da PA: '))
razao = int(input('Digite a razão: '))
print('10 primeiros termos de uma Progressão Aritmérica')
print(primeiro_termo)
seg = primeiro_termo
for i in range(9):
    print(primeiro_termo + razao)
    primeiro_termo = primeiro_termo+razao

#outra forma:
for i in range (seg, seg+(razao*10),razao):
    print(i)
