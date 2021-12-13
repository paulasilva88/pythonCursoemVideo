'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%'''

salary = float(input('Digite o seu salário atual para saber quanto você terá de aumento: '))
if salary>1250:
    print('O aumento do seu salário de R${:.2f} será de R${:.2f}, então salário será de R${:.2f}'.format(salary, salary*0.10, salary*1.10))
else:
    print('O aumento do seu salário de R${:.2f} será de R${:.2f}, então salário será de R${:.2f}'.format(salary,
                                                                                                         salary * 0.15,
                                                                                                         salary * 1.15))