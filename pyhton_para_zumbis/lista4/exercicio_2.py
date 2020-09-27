''' Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR 
e os números ímpares na lista IMPAR. Imprima as trêslistas.'''

import random

lista = []
lista_par = []
lista_impar = []
c = 0
while c < 20:
    n = (random.randint(1,100))
    lista.append(n)
    c = c + 1
    if n%2 == 0:
        lista_par.append(n)
    elif n%2 != 0:
        lista_impar.append(n)
print(f'\nLista:{lista}')
print(f'\nLista par: {lista_par}')
print(f'\nLista ímpar: {lista_impar}')

