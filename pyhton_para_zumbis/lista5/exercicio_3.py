''' Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7'''

divisíveis_2_7 = []
for n in range(1067, 3627):
    if n % 2 == 0  and n % 7 == 0:
        divisíveis_2_7.append(n)
print(f'\n A qtd de nºs divisíveis por 2 e 7 entre 1067 e 3627 são: {len(divisíveis_2_7)}')