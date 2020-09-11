print('=== VERIFICAÇÃO TRIÂNGULO ===')
l1 = float(input('Insira o 1º lado: '))
l2 = float(input('Insira o 2º lado: '))
l3 = float(input('Insira o 3º lado: '))
if  l1 > l2 + l3 or l2 > l3 + l1 or l1 > l3 + l2: 
    print('\nOs valores não formam um triângulo!')
elif l1 == l2 and l2 == l3:
    print('\nTriângulo equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('\nTriângulo isósceles')
else: 
    print('\nTriângulo escaleno')