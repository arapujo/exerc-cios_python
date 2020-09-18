''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas '''

print('=== QUANTIDADE DE TINTAS ===')
area = float(input('Informe o tamanho da área a ser pintada: '))
qtd_litro = (area / 3)
if qtd_litro % 18 == 00:
    qtd_lata = qtd_litro / 18
else:
    qtd_lata = int(qtd_litro/18) + 1
preco = qtd_lata * 80
print(f'\n Quantidade de latas: {qtd_lata} \nO preço total é: R${preco}')