print(' === REDUÇÃO TEMPO DE VIDA PELO FUMO === ')
qtdCigarro = int(input('Informe a quantidade de cigarro fumados por dia: '))
qtdAno = float(input('Informe a quantidade de anos fumando: '))
qtdCigarroTotal = qtdCigarro * (qtdAno * 365)
qtdMinutos = qtdCigarroTotal * 10
qtdDia = (qtdMinutos/60)/242
print(f'\nQuantidade de cigarro fumados: {qtdCigarroTotal} \nQuantidade de dias perdidos: {qtdDia:.2f}')
