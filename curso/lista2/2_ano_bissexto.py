print('=== ANO BISSEXTO ===')
ano = int(input('Insira o ano: '))
if ano % 100 != 00 and ano % 4 == 0 or ano % 100 !=0 and  ano % 4 == 0 and ano % 400 == 00:
    print('Ano bissexto!')
else:
    print('Ano não é bissexto')

