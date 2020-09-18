''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. '''

print('=== SENHA USUÁRIO ===')
nome_usuario = input('Insira seu nome: ')
senha_usuario = input('Insira senha: ')
while nome_usuario == senha_usuario:
    print('\nSenha não pode ser igual usuário!')
    break
else: 
    print('\nUsuário e senha válido!')