'''A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Até 19 anos: JUNIOR
-  Até 20 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date
idade = date.today().year - int(input('Em que ano você nasceu?'))
print(idade)
if idade <=9:
    print(('Sua categoria é MIRIM'))
elif idade<=14:
    print('Sua categoria é INFANTIL')
elif idade<=19:
    print('Sua categoria é JÚNIOR')
elif idade<=20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
