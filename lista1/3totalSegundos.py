print(' === TOTAL DE SEGUNDOS === ')
numeroDia = int(input('Insira a quantidade de dias: '))
numeroHora = float(input('Insira a quantidade de horas: '))
numeroMinuto = float(input('Insira a quantidade de minutos: '))
numeroSegundo = float(input('Insira a quantidade de segundos: '))
conversaoDia = numeroDia * 86400
conversaoHora = numeroHora * 3600
conversaoMinuto = numeroMinuto * 60
totalSegundos = (conversaoDia + conversaoHora + conversaoMinuto + numeroSegundo)
print(f'\nTotal de segundos: {totalSegundos}s')
