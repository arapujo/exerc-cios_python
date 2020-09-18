''' Faça um Programa que leia três números e mostre o maior deles '''

print('=== MAIOR NÚMERO ===')
n1 = float(input('Insira o 1º nº: '))
n2 = float(input('Insira o 2º nº: '))
n3 = float(input('Insira o 3º nº: '))
if n1 > n2 and n1 > n3:
    print(f'\nMaior número {n1}')
elif n2 > n1 and n2 > n3:
    print(f'\nMaior número {n2}')
else:
    print(f'\nMaior número: {n3}')