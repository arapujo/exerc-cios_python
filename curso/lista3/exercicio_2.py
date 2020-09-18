print('=== SENHA USUÁRIO ===')
nome_usuario = input('Insira seu nome: ')
senha_usuario = input('Insira senha: ')
while nome_usuario == senha_usuario:
    print('\nSenha não pode ser igual usuário!')
    break
else: 
    print('\nUsuário e senha válido!')