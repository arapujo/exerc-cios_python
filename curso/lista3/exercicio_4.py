print('=== SEQUÊNCIA DE FIBONACCI')
n = int(input('Insira um número: '))
a, b = 1, 1
c = 1
while c <= n - 2:
    a, b = b, a + b
    c = c + 1
print(f'Seu número de fibonacci é: {b} ')