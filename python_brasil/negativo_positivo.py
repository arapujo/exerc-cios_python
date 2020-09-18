''' Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''

print('=== POSITIVO OU NEGATIVO ===')
n = float(input('Insira um número: '))
if n >= 0:
    print(f'\n{n} é positivo.')
else:
    print(f'\n{n} é negativo.')