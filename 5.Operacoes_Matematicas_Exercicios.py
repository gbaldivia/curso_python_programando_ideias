"""
1 - Realizar a média das notas de quatro alunos
"""
num1 = float(input('Primeira nota: '))
num2 = float(input('Segunda nota: '))
num3 = float(input('Terceira nota: '))
num4 = float(input('Quarta nota: '))

print(f'A média das notas é {(num1 + num2 + num3 + num4)/4}')

print(f' ')
print(f' ')
print(f' ')
print(f' ')

"""
2 - Converter uma temperatura de ºC para ºF e para ºK.
ºF = ºC * 1.8 + 32
ºK = ºC + 273.15
"""

celsius = float(input('Temperatura em graus Celsius: '))

print(f'A temperatura em graus Fahrenheit é {celsius * 1.8 + 32}')
print(f'A temperatura em graus Kelvin é {celsius + 273.15}')

print(f' ')
print(f' ')
print(f' ')
print(f' ')

"""
3 - Criação de personagem de mundo fictício, apresentando opções de acordo com os tipos de variáveis:
- Cor do cabelo (string)
- Cor da pele (string)
- Casse: Guerreiro, Mago, Arqueiro, Élfo, Anão, Bardo (string)
- Idade (int)
- Altura (float)
- Habilidade Especial (string)

Imprima para o usuário o personagem completo.
"""
print(f'----------------------- BEM VINDO A UM NOVO UNIVERSO-----------------------')

print(f'Crie o seu peronagem!')

nome = input('Nome do personagem: ').title()
cabelo = input('Digite a cor do cabelo: ').lower()
pele = input('Digite a cor da pele do personagem: ').lower()
classe = input('Digite a classe do personagem: ').lower()
idade = int(input('Digite a idade do personagem: '))
altura = float(input('Digite a altura do persnagem: '))
skills = input('Digite qual será a habilidade especial do personagem: ').lower()
defeat = input('Digite qual será a fraqueza do personagem: ').lower()

print(f'{nome} pertencente à classe {classe}, tem pele {pele} e cabelos {cabelo}. \n'
      f'{nome} tem {idade} anos e {altura} metros de altura. \n'
      f'{nome} tem a grande habilidade de {skills}, porém em contrapartida sua grande fraqueza é {defeat}.')
