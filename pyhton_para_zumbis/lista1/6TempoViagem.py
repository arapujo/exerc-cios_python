''' Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem '''

print(' === TEMPO DE VIAGEM === ')
distancia = float(input('Informe a distância percorrida: '))
velocidade_media = float(input('Informe a velocidade média: '))
tempo_percorrido = distancia / velocidade_media
print(f'\nO tempo de viagem foi: {tempo_percorrido}')
