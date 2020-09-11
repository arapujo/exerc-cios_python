print('=== Cálculo Salário ===')
valorHora = float(input('Informe o valor ganho por hora: '))
trabalhoHora = float(input('Informe o nº de hora trabalhadas: '))
salarioBruto = valorHora * trabalhoHora
descInss = salarioBruto * 0.08
descIr = salarioBruto * 0.11
descSin = salarioBruto * 0.05
descontoTotal = descInss + descIr + descSin
salarioLiquido = salarioBruto - descontoTotal
print(f'\nSalário Bruto: {salarioBruto} \nDesconto INSS: {descInss} \nDesconto IR: {descIr} \nDesconto Sindicato: {descSin} \nDescontos: {descontoTotal:.2f} \nSalário Líquido: {salarioLiquido}')