''' Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 '''

print(' === CONVERSÃO CELSIUS => FAHRENHEIT === ')
valor_celsius = float(input('Informe a temperatura em °C: '))
conversao = (1.8 * valor_celsius) + 32
print(f'\n{valor_celsius}°C convertido em Fahrenheit é {conversao}°F')
