print('=== SENHA USUÁRIO ===')
nomeUsuario = input('Insira seu nome: ')
senhaUsuario = input('Insira senha: ')
while nomeUsuario == senhaUsuario:
    print('\nSenha não pode ser igual usuário!')
    break
else: 
    print('\nUsuário e senha válido!')