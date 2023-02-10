"""
1 - Crie um sistema de cadastro e login de um site utilizando username e senha informados pelo usuário.
"""

print('---------------------------- Bem-vindo ao cadastro do site!')
user = input('Digite o seu login: ')
key = input('Digite sua senha: ')
login = False

print('---------------------------- LOGIN')

if input('Digite seu login: ') == user and input('Digite sua senha para logar: ') == key:
    login = True
    print(f'\n Seja bem-vindo (a), {user}.')
else:
    login = False
    print('\n Senha errada, tente novamente.')
