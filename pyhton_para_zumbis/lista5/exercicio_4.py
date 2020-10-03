''' Questão D.
Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7.
Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?'''

c = 0
for i in (range(18644, 33087)):
    if '2' in str(i) and '7' not in str(i):
        c = c  + 1
print(f'\nExistem {c} nº sortudos entre 18644 e 33087')