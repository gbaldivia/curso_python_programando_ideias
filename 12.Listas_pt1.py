"""
Listas - Coleção de dados muito poderosa e importante, diferente de tudo que você já viu

Vetores e Matrizes: apenas um tipo de dado, tamanho único.

Listas: são dinâmicas, podem receber qualquer tipo de dado. E tem tamanho limitado à memória dispnível no PC.

Sintaxe: [elemento1, elemento2, ..., elementoN]

# -----------------------------------------------------------
# Adicionar 1 elemento por vez na lista - Append
# Obs: Adiciona o objeto

print(lista2)
lista2.append(6)
print(lista2)
lista2.append(10)
lista2.append('Maria Joaquina')
lista2.append('Molho de Alho')
lista2.append(True)
print(lista2)
lista2.append([2, 4, 6, 8])
print(lista2)

# -----------------------------------------------------------
# Adicionar vários elementos na lista: Extend
# Obs: recebe apenas um objeto iterável por vez e adiciona os elementos um a um na lista
lista5.extend(['abacaxi', 1.98, 'Kg'])
print(lista5)

lista5.extend([1, True], [0, False]) #Erro
lista5.extend(12) #Erro

# -----------------------------------------------------------
# Adicionar valores de uma lista: Insert
# Adiciona um valor de um determinado índice da lista
# Obs: esse comando não substitui o valor original, apenas desloca para a direita
print(lista4)
lista4.insert(1, 'Aqui')
print(lista4)

# -----------------------------------------------------------
# Concatenar duas ou mais listas
listaSomada = lista2 + lista4
print(lista2)
print(lista4)
print(listaSomada)
lista2.extend(lista4)
print(lista2)

# -----------------------------------------------------------
# Converter strings em listas: Split
# Cria uma lista separando uma string por seus espaços (' '). Esse é o modo padrão.
frase = 'Hoje é um novo dia, de um novo tempo, que começou'
lista9 = frase.split()
print(lista9)

# Obs: É possível indicar o parâmetro de separação
lista9 = frase.split(',')
print(lista9)

lista9 = frase.split('novo')
print(lista9)

# -----------------------------------------------------------
# Converter listas em string: Join
# Cria uma string juntando os elementos de uma lista
lista10 = ['Silvio', 'Santos', 'vem', 'ai.']
frase = ' '.join(lista10)
print(frase)

frase = '@'.join(lista10)
print(frase)

# -----------------------------------------------------------
# Contar elementos da lista
print(len(lista7))

# -----------------------------------------------------------
#Verificar se determinado elemento está em uma lista
if 'X' in lista7:
    print(True)
else:
    print(False)

# Outra forma de verificar se o elemento está na lista:
print('X' in lista7)
# Retorna True se está na lista e False se não está na lista

# -----------------------------------------------------------
# Obter a quantidade de vezes que um valor se repete na lista - Count
print(lista6)
quantidade = lista6.count('t')
print(f'Eu encontrei {quantidade} vez/vezes')

# -----------------------------------------------------------
# Ordenar a lista - Sort
listaMaluca = [21, 232, 123, 434, 1, 2, 42, 6, 10, 83, 567]
print(listaMaluca)

listaMaluca.sort()
print(listaMaluca)

listaDoida = ['y', 'uy', 'a', 'peixe']
print(listaDoida)
listaDoida.sort()
print(listaDoida)

# -----------------------------------------------------------
# Inverter uma lista
print(lista7)
lista7.reverse()
print(lista7)

# Obs: [Início:Fim:Passo]
print(lista7)
print(lista7[2:])
print(lista7[2:6])
print(lista7[2:7:2])

# -----------------------------------------------------------
# Acessar elementos de uma lista
print(lista7[1])
print(lista7[-1])

for ind in range(0, 3):
    print(lista7[ind])

# -----------------------------------------------------------
# Substituit eletemento de uma lista
print(lista7)
lista7[1] = False
lista7[4] = 'Vodka'
print(lista7)

# -----------------------------------------------------------
# Remover elementos e uma lista: Pop
# Remove e retorna o último elemento de uma lista
print(lista2)
print(lista2.pop())
print(lista2)

# Obs: é possível indicar o índice do valor a ser removido
# Obs: os valores da direita são deslocados para a esquerda
print(lista7)
lista7.pop(5)
print(lista7)

# -----------------------------------------------------------
# Repetir elementos de uma lista
print(lista4)
lista4 = 5 * lista4
print(lista4)

# -----------------------------------------------------------
# Limpar uma lista - Clear
print(lista7)
lista7.clear()
print(lista7)
"""
# Exemplos de declaração de listas:
lista1 = []
lista2 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]
lista3 = [3.4, 23.43, 5234.23, 432.86]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Corinthians 1910')
lista7 = [43, True, 23.1, 'abacate', 'Rússia', 12, 'X', False, [1, 3, 5, 7]]

cor = 'azul'
animal = 'pavão'
numero = 42
lista8 = [cor, animal, numero]
