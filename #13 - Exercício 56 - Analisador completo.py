'''Desenvolva um programa que leia o nome,a idade e o sexo de 4
pessoas. No final do programa, mostre:
- A média da idade do grupo
-  Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos'''
soma_idades = 0
idade_mais_velho = 0
m_menores = 0
for i in range(4):
    print('Dados da pessao {}'.format(i+1))
    nome = str(input('Nome: Digite '))
    idade = int (input('Idade: '))
    sexo = str(input('Sexo: (Digite f para feminino e m para masculino)'))
    soma_idades = soma_idades + idade
    if sexo =='m':
        if idade > idade_mais_velho:
            mais_velho = nome
            idade_mais_velho = idade
            print('Nome do homem mais velho até agora {}'.format(nome))
        elif idade==idade_mais_velho:
            mais_velho = [mais_velho, nome]
    elif sexo == 'f':
        if idade < 20:
            m_menores = m_menores + 1
print('A média das idades das pessoas é {}.'.format(soma_idades/4))
print('O nome do homem mais velho é {}.'.format(mais_velho) if idade_mais_velho>0 else 'Não foram inseridos dados sobre homens')
print('Há {} mulheres com menos de 20 anos.'.format(m_menores) if m_menores>0 else 'Não foram adicionados dados sobre mulheres menores de 20 anos')