print('=== QUANTIDADE DE TINTAS ===')
area = float(input('Informe o tamanho da area a ser pintada: '))
qtdLitro = (area / 3)
if qtdLitro % 18 == 00:
    qtdLata = qtdLitro / 18
else:
    qtdLata = round(qtdLitro/18)
    if round(qtdLitro/18) < qtdLitro/18:
        qtdLata = round(qtdLitro/18) + 1
preco = qtdLata * 80
print(f'\n Quantidade de latas: {qtdLata} \nO preço total é: R${preco}')