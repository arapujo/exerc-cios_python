''' Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''

print('=== FEMININO OU MASCULINO ===')
letra = input('Digite uma letra: ')
letra_comparacao = letra.upper()
if letra_comparacao == "F":
    print('\nF - Feminino')
elif letra_comparacao == "M":
    print('\nM - Masculino')
else:
    print('\nSexo Inválido!')