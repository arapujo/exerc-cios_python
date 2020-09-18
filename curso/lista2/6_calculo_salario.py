print('=== Cálculo Salário ===')
valor_hora = float(input('Informe o valor ganho por hora: '))
trabalho_hora = float(input('Informe o nº de hora trabalhadas: '))
salario_bruto = valor_hora * trabalho_hora
desc_inss = salario_bruto * 0.08
desc_ir = salario_bruto * 0.11
desc_sin = salario_bruto * 0.05
desconto_total = desc_inss + desc_ir + desc_sin
salario_liquido = salario_bruto - desconto_total
print(f'\nSalário Bruto: {salario_bruto} \nDesconto INSS: {desc_inss} \nDesconto IR: {desc_ir} \nDesconto Sindicato: {desc_sin} \nDescontos: {desconto_total:.2f} \nSalário Líquido: {salario_liquido}')