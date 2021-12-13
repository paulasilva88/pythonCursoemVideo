'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizandp um laço for'''
numero = int(input('Digite um número que você quer saber a tabuada: '))
print('''{}
{}TABUADA{}'''.format('-'*47,'-'*20,'-'*20 ))
for i in range(1,11):
    print('{} x {} = {}'.format(numero, i, numero*i))