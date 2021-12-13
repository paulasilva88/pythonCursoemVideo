'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar e quanto tempo falta;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

Seu promograma também deverá mostrar o tempo que falta ou que passou
do prazo.'''

from datetime import date
ano_atual = date.today().year
print('''Olá, jovem! Bem vindo ao sistema do serviço militar!
{}'''. format('-'*60))
ano = int(input('Qual o ano do seu nascimento? '))
idade = ano_atual-ano
if idade<18:
    print('\033[34mVocê ainda não tem idade para se alistar, faltam {} anos!'.format(18-idade))
elif idade>18:
    print('\033[31mJá se passou {} anos do seu tempo de alistamento'.format(idade-18))
else:
    print('\033[34mVocê já tem {} anos, é hora de se alistar!'.format(idade))