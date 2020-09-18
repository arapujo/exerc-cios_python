''' Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''

print('=== QUANTIDADE DE CENTENAS, DEZENAS E UNIDADES ===')
numero = int(input('Insira um número inteiro menor que 1000: '))
n = str(numero)
if numero < 1000 and numero > 100:
    c = str(n[0])
    d = str(n[1])
    u = str(n[2])
    print(f'\n{n} = {c} centenas, {d} dezenas e {u} unidades.')
elif numero < 100 and numero > 10:
    d = str(n[0])
    u = str(n[1])
    print(f'\n{n} = 0 centenas, {d} dezenas e {u} unidades.')
elif numero < 10:
    u = str(n[0])
    print(f'\n{n} = 0 centenas, 0 dezenas e {u} unidades.')
else:
    print('Número inválido!')

