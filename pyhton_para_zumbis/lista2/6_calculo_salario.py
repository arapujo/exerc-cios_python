''' Faça um Programa que pergunte quanto você
ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato
e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b.- IR (11%) : R$
c.- INSS (8%) : R$
d.- Sindicato ( 5%) : R$
e. = Salário Liquido : R$ '''

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