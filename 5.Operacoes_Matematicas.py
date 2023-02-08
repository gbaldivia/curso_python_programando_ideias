"""
Operações Matemáticas
"""
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

print(f'Soma: {num1 + num2}')

print(f'Subtração: {num1 - num2}')

print(f'Multiplicação: {num1 * num2}')

print(f'Divisão: {num1 / num2}')

print(f'Divisão Inteiro: {num1 // num2}')

print(f'Potenciação: {num1 ** num2}')

"""
Operações com Strings
"""
nome = 'Geremias'
print(nome * 3)

sobrenome = 'da Silva'

nomeCompleto = nome + sobrenome

print(nomeCompleto)

"""
Operação com Boolean

True = 1
False = 0
"""

print(True * False)
print(True * True)
print(True + True)
print(True - False)
print(True ** 2)

"""
Casting: conversão de um tipo de dado em outro

String <=> Inteiro
String <=> Float
Inteiro <=> Float
Boolean <=> Inteiro
Boolean <=> Float
Boolean <=> String

Para String: str()
Para Inteiro: int()
Para Float: float()
Para Boolean: bool()

"""
print(bool('urso'))
print(bool(92))
