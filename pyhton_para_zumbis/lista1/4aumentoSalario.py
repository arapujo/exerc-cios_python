''' Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário '''

print(' === AUMENTO SALÁRIO === ')
valor_salario = float (input('Insira o valor do salário: '))
porcentagem_aumento = float (input('Insira a porcentagem do aumento: '))
valor_aumento = (porcentagem_aumento/100) * valor_salario
salario_novo = valor_salario + valor_aumento
print(f'\nValor do aumento: R${valor_aumento} \nSalário reajustado: R${salario_novo}')
