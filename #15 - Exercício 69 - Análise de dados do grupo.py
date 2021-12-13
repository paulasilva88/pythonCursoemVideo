'''Crie um programa que leia a idade e o sexo de várias pesoas.
A cada pessoa casatradas, o programa deverá perguntar se ao usuário
quer ou não continuar, no final, mostre:

A) Quntas pessoas tem mais de 18 anos.

B) Quantos homens foram cadastrados.

C) Quantas mulheres tem menos de 20 anos.
'''
maiores = homens = mulheres_20 = 0 #Atribuição de todas os contadores
while True:
    idade = int(input('Idade: '))
    #sexo = str(input('Sexo: [F/M] ')).strip().upper()
    #while sexo != 'F' and sexo != 'M':
        #sexo = str(input('Sexo: [F/M]')).strip().upper()

    #Outra forma de validação:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).strip().upper()
    if idade>=18:
        maiores +=1
    if sexo =='F' and idade <20:
        mulheres_20 +=1
    if sexo =='M':
        homens +=1
    decisao = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()
    while decisao  !='S' and decisao!= 'N':
        decisao = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()
    if decisao == 'N':
        break
print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos.')
print(f'Foram cadastradados {homens} homens.')
print(f'Foram cadastradas {mulheres_20} mulheres com menos de 20 anos')
