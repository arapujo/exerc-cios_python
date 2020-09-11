print(' === DESCONTO - PRODUTO === ')
precoProduto = float(input('Insira o preço: '))
percentualDesconto = float(input('Insira o valor do desconto: '))
valorDesconto = (percentualDesconto/100) * precoProduto
valorNovo = precoProduto - valorDesconto
print(f'\nValor desconto: R${valorDesconto} \nValor produto com desconto: R${valorNovo}')

