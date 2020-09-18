print(' === REDUÇÃO TEMPO DE VIDA PELO FUMO === ')
qtd_cigarro = int(input('Informe a quantidade de cigarro fumados por dia: '))
qtd_ano = float(input('Informe a quantidade de anos fumando: '))
qtd_cigarro_total = qtd_cigarro * (qtd_ano * 365)
qtd_minutos = qtd_cigarro_total * 10
qtd_dia = (qtd_minutos/60)/242
print(f'\nQuantidade de cigarro fumados: {qtd_cigarro_total} \nQuantidade de dias perdidos: {qtd_dia:.2f}')
