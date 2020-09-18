print(' === DESCONTO - PRODUTO === ')
preco_produto = float(input('Insira o preço: '))
percentual_desconto = float(input('Insira o valor do desconto: '))
valor_desconto = (percentual_desconto/100) * preco_produto
valor_novo = preco_produto - valor_desconto
print(f'\nValor desconto: R${valor_desconto} \nValor produto com desconto: R${valor_novo}')

