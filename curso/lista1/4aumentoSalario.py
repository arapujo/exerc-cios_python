print(' === AUMENTO SALÁRIO === ')
valorSalario = float (input('Insira o valor do salário: '))
porcentagemAumento = float (input('Insira a porcentagem do aumento: '))
valorAumento = (porcentagemAumento/100) * valorSalario
salarioNovo = valorSalario + valorAumento
print(f'\nValor do aumento: R${valorAumento} \nSalário reajustado: R${salarioNovo}')
