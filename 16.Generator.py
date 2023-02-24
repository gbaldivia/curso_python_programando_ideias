"""
Generators

— Tuple Comprehension
Gera um objeto gnerator a partir do processamento de uma coleção de dados.

Sintaxe: (operação/função for elemento in iterável)

Após o objeto generator ser iterado, ele é automaticamente apagado da

# Exemplos de generators
# Exemplo 1
numeros = list(range(1, 11))
maiores = (numero for numero in numeros if numero > 5)

print(numeros)
print(type(maiores))
print(maiores)

for i in maiores:
    print(i, end=' ')

# Exemplo 2
nomes = ('Pedro', 'Tiara', 'Lucas', 'Gustavo', 'Ana')
nome5 = (nome * 2 if len(nome) == 5 else nome for nome in nomes)
print(f'\n{type(nome5)}')
print(nome5)
listaNova5 = list(nome5)
print(listaNova5)
"""
# Comparação de ocupação e memória

from sys import getsizeof

print(getsizeof('Gabriela Baldivia Soncini'))  # Retorna a memória ocupada em bytes
print(getsizeof(10))
print(getsizeof([num for num in range(1, 1001)]))  # Retorna a memória de um list comprehension
print(getsizeof(num for num in range(1, 1001)))  # Retorna a memória de um generator
