'''Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 
Imprima os três vetores.'''

import random

lista1 = []
lista2 = []
lista3 = []

for n in range(10):
    lista1.append(random.randint(1 ,100))
    lista2.append(random.randint(1 ,100))
    lista3.append(lista1[n])
    lista3.append(lista2[n])
print(f'\nLista 1: {lista1}')
print(f'\nLista 2: {lista2}')
print(f'\nLista 3: {lista3}')