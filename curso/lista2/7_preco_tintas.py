print('=== QUANTIDADE DE TINTAS ===')
area = float(input('Informe o tamanho da área a ser pintada: '))
qtd_litro = (area / 3)
if qtd_litro % 18 == 00:
    qtd_lata = qtd_litro / 18
else:
    qtd_lata = int(qtd_litro/18) + 1
preco = qtd_lata * 80
print(f'\n Quantidade de latas: {qtd_lata} \nO preço total é: R${preco}')