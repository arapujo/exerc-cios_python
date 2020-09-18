''' Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calculeo total em segundos.'''

print(' === TOTAL DE SEGUNDOS === ')
numero_dia = int(input('Insira a quantidade de dias: '))
numero_hora = float(input('Insira a quantidade de horas: '))
numero_minuto = float(input('Insira a quantidade de minutos: '))
numero_segundo = float(input('Insira a quantidade de segundos: '))
conversao_dia = numero_dia * 86400
conversao_hora = numero_hora * 3600
conversao_minuto = numero_minuto * 60
total_segundos = (conversao_dia + conversao_hora + conversao_minuto + numero_segundo)
print(f'\nTotal de segundos: {total_segundos}s')
