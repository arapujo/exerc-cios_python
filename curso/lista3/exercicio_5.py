print('=== ALGORITMO DE EUCLIDES ===')
n = int(input('Insira o 1º nº: '))
m = int(input('Insira o 2º nº: '))
r2 = 0
q2 = 0
while n % m != 0:
    q = n / m
    r = n % m
    q2 = m / r
    r2 = m % r

print(f'{r2}')