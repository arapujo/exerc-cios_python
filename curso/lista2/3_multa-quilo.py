print('=== MULTA EXCEDENTE QUILO ===')
peso = float(input('Insira o peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'\nExcesso: {excesso} kg \nMulta: {multa}')
else:
    print('\nExcesso: 0 \nMulta: 0')