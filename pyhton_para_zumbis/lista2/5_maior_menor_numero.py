''' Faça um Programa que leia três números e mostre o maior e o menor deles '''

print('=== MAIOR E MENOR NÚMERO ===')
n1 = float(input('Insira o 1º nº: '))
n2 = float(input('Insira o 2º nº: '))
n3 = float(input('Insira o 3º nº: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'\nMaior número {n1} \nMenor número {n3}')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'\nMaior número {n1} \nMenor número {n2}')
elif n2 > n1 and n2 > n3 and n1 > n3 :
    print(f'\nMaior número {n2} \nMenor número {n3}')
elif n2 > n1 and n2 > n3 and n3 > n1 :
    print(f'\nMaior número {n2} \nMenor número {n1}')
elif n3 > n1 and n3 > n2 and n2 > n1:
     print(f'\nMaior número {n3} \nMenor número {n1}')
else:
    print(f'\nMaior número: {n3} \nMenor número {n2}')