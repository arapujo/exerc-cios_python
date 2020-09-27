''' Sorteie 10 inteiros entre 1 e 100 para uma lista e descubrao maior e o menor valor, sem usaras funções max e min. '''

import random

lista = []
c = 0
while c < 10:
    n = (random.randint(1,100))
    c = c + 1
    lista.append(n)
print(lista)
lista.sort()    
print(f'\nMaior número: {lista[-1]} Menor número: {lista[0]}')
   

   
    


