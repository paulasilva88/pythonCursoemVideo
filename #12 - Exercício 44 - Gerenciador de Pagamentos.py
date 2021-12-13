'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preõ normal, e condição de pagamento:

-à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

valor = float(input('Informe o valor a ser pago: '))
forma_de_pagamento = int(input('''De que forma você irá pagar? Digite o número correspondente: 
1 - À vista em dinheiro ou cheque (-10%)
2 - À vista no cartão (-5%)
3 - em até 2x no cartão
4 - 3x ou mais no cartão(+20%)
'''))
if forma_de_pagamento ==1:
    print('O valor que você irá pagar é R${:.2f}'.format(valor*0.9))
elif forma_de_pagamento == 2:
    print('O valor que você irá pagar é R${:.2f}'.format((valor*0.95)))
elif forma_de_pagamento == 3:
    print('O valor que você irá pagar é R${:.2f}'.format(valor))
elif forma_de_pagamento == 4:
    print('O valor que você irá pagar é R${:.2f}'.format(valor*1.2))