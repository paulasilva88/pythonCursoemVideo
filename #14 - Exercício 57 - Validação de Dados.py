''''Faça um porhrama que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um
valor correto'''

sexo = str(input('Digite o seu sexo (F/M): ')).upper()
while sexo != 'F' and sexo!= 'M':
    sexo = str(input('Digite o seu sexo (F/M): ')).upper()