"""
Estruturas condicionais

if, elif, else
"""

"""
#testar altura para brinquedo de parque
altura = float(input('Digite sua altura: '))

if altura < 1.6:
    print('Não permitido a entrada')
else:
    print('Siga em frente, você pode brincar!')
"""

"""
#Consultar média final para aprovação

nota = float(input('Digite a nota: '))

if nota >= 6:
    print('Pode curtir suas férias!')
else:
    print('Você tem exame semana que vem.')
"""

"""
#Determinar se o número é par ou ímpar
num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')
"""

"""
#Utilizando outros tipos de dados

pais = input('Digite um país que você deseja visitar: ')

if pais == 'Noruega':
    print('Ah não, muito frio!')
elif pais == 'China':
    print('Ah não, muito longe!')
elif pais == 'Austrália' :
    print('Ah não, muito canguru!')
else:
    print('Vamos!')
"""

"""
#Utilizando outros tipos de dados

login = False
senha = 'Caneta1'

key = input('Digite sua senha: ')

if key == senha:
    login = True
else:
    print('Senha incorreta.')

if login == True:
    print('Bem-vindo admin.')
else:
    print('Tente novamente.')
"""
#Cuidado com variáveis globais e locais

senha = 'Caneta1'
key = 'Caneta1'

if key == senha:
    login = True
else:
    login = False
    print('Senha Incorreta')

if login:
    print('Seja bem-vindo admin.')
else:
    print('Senha incorreta.')
