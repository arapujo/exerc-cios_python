''' Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''

print('=== VOGAL OU CONSOANTE ===')
letra = input('Insira uma letra: ')
letra_comparacao = letra.lower()
if letra_comparacao == "a" or letra_comparacao == "e" or letra_comparacao == "i" or letra_comparacao == "o" or letra_comparacao == "u":
    print(f'\nLetra {letra} é uma vogal.')
else:
    print(f'\nLetra {letra} é uma consoante.')