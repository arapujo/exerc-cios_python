print('=== TAXA DE CRESCIMENTO ===')
taxa_a = 80000
taxa_b = 200000
ano = 0
while taxa_a <= taxa_b:
    taxa_a = taxa_a + (taxa_a * 0.03)
    taxa_b = taxa_b + (taxa_b * 0.015)
    ano = ano + 1
print(f'Ano:{ano}')
    
    

