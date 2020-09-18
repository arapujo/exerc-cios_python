''' Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. '''

print(' === CÁLCULO CARRO ALUGADO === ')
qtd_km = float(input('Informe a quantidade de KM rodados: '))
qtd_dia = float(input('Informe por quanto dias o carro foi alugado: '))
preco_total = (60 * qtd_dia) + (0.15 * qtd_km)
print(f'\nQuantidade de dias: {qtd_dia} \nQuantidade de km: {qtd_km} \nPreço total: {preco_total}')
