"""
Listas - pt2

# ----------------------------------------------------------------
# Obs: Listas são ordenadas, ou seja, seus índices são importante.
listaNova = []
for numero in range(1, 11):
    listaNova.append(numero)
print(listaNova)

listaNova2 = list(range(1, 11))
print(listaNova2)

# ----------------------------------------------------------------
# Percorrer listas (iterar)
# FOR
for elemento in lista2:
    print(elemento, end=' ')

print('\n')
total = 0
for elemento in lista2:
    total += elemento

print(total/len(lista2))

# ----------------------------------------------------------------
# Percorrer listas (iterar)
# While
total = 0
cont = 0
while len(lista2) != 0:
    total += lista2.pop()
    cont += 1

print(total/cont)

# ----------------------------------------------------------------
# Obter indices da lista
jogos = ['Sonic', 'Super Mario', 'GTA', 'GoW', 'PES']
for indice, jogo in enumerate(jogos):
    print(indice, jogo)

# retorna índice do primeiro valor 4 encontrado na lista
print(lista2.index(4))

#Busca O VALOR 5 a partir do índice 4
print(lista2.index(5, 4))

#Busca o valor 5 entre os índices 3 e 6
print(lista2.index(5, 3, 6))

# ----------------------------------------------------------------
# Descompactar listas
animal, cor, letra = lista5
print(animal, cor, letra)

# ----------------------------------------------------------------
# Funções para trabalhar com listas
# Obs: apenas para inteiros ou floats
print(sum(lista2))
print(max(lista2))
print(min(lista2))

# ----------------------------------------------------------------
# Arredondar os valores da lista
listaPlana = [1.22, 2.984367, 9.23184832]

for elemento in listaPlana:
    print(round(elemento, 2))

# ----------------------------------------------------------------
# Obter o módulo de uma lista
listaPessimista = [-1, -2, -5, -10, 1000]

for numero in listaPessimista:
    print(abs(numero))

# ----------------------------------------------------------------
# Copiar uma lista - Deep Copy
# Obs: copia as listas e as torna independente entre si, se mudar uma, não afeta a outra.
print(lista2)
lista1 = lista2.copy()
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

# ----------------------------------------------------------------
# Copiar lista - Shallw Copy
# Copia as listas e as conecta. Qualquer modificação em uma modifica a outra
print(lista2)
lista1 = lista2
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)


"""

# Exemplos de declaração de listas:
lista1 = []
lista2 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]
lista3 = [3.4, 23.43, 5234.23, 432.86]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Corinthians 1910')
lista7 = [43, True, 23.1, 'abacate', 'Rússia', 12, 'X', False, [1, 3, 5, 7]]

# ----------------------------------------------------------------
# Matrizes em Python
# Cada lista interna é uma linha da matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])
print(matriz[1])
print(matriz[2])

for linha in matriz:
    print(f'\n{linha}')
    for elemento in linha:
        print(elemento, end=' ')

print(f'\n\n{matriz[1][2]}')

# ----------------------------------------------------------------
# Jogo da velha
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # Matriz 3x3
print(matriz[0])
print(matriz[1])
print(matriz[2])

LP1 = int(input('Escolha a linha: '))
CP1 = int(input('Escolha a coluna: '))
matriz[LP1][CP1] = 'X'

LP2 = int(input('Escolha a linha: '))
CP2 = int(input('Escolha a coluna: '))
matriz[LP2][CP2] = 'O'

for linha in matriz:
    print(linha)
