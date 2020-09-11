print('=== QUANTIDADE DE TINTAS ===')
area = float(input('Informe o tamanho da área a ser pintada: '))
qtdLitro = (area / 3)
if qtdLitro % 18 == 00:
    qtdLata = qtdLitro / 18
else:
    qtdLata = int(qtdLitro/18) + 1
preco = qtdLata * 80
print(f'\n Quantidade de latas: {qtdLata} \nO preço total é: R${preco}')