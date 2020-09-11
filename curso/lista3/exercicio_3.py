print('=== TAXA DE CRESCIMENTO ===')
taxaA = 80000
taxaB = 200000
ano = 0
while taxaA <= taxaB:
    taxaA = taxaA + (taxaA * 0.03)
    taxaB = taxaB + (taxaB * 0.015)
    ano = ano + 1
print(f'Ano:{ano}')
    
    

