''' Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''

print('ASSASSINO, CÚMPLICE, SUSPEITO OU SUSPEITO')
print('\nRespondas as seguintes perguntas com SIM ou NÃO.')
p1 = input('\nTelefonou para a vítima? ')
p2 = input('\nEsteve no local do crime? ')
p3 = input('\nMora perto da vítima? ')
p4 = input('\nDevia para vítima? ')
p5 = input('\nJá trabalhou com a vítima? ')
if p1.upper() == "SIM" and 