''' Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides '''

print('=== ALGORITMO DE EUCLIDES ===')
n1 = int(input('Insira o 1º nº: '))
n2 = int(input('Insira o 2º nº: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print(f'\nMDC é {n2}')