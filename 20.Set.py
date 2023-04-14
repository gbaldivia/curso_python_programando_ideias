"""
Sets - Conjuntos

Conjuntos se assemelha à teoria de conjuntos.
- Não são ordenados. Assim como os dicionários.
- Não aceitam elementos repetidos.
- São representados por chaves {}, igual ao dicionário, porém não possuem a relação chave -> dado. É apenas dado.

Vantagem de utilizar conjuntos:
- Utilização de formas otimizadas de realizar funções específicas que só ele possui, como intersecção, união, etc.

Quanto utilizar?
- Quando não precisa se preocupar com ordenação e repetição de elementos.
----------------------------------------------------------------------------------------------
Como declara:
Forma 1 - Mais usada:
nome = {dado1, dado2, dado3, dado4, ...}

conjunto = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6}
print(conjunto)
print(type(conjunto))

Forma 2 - Função set
conjunto = set(iteravel)

conjunto = set([1, 2, 3, 4])
print(conjunto)
print(type(conjunto))

Forma 3 - Conjunto vazio
conjunto = set()
----------------------------------------------------------------------------------------------
Aplicando Conjuntos no FOR
pares = {2, 4, 6, 8, 10, 12, 14}
for num in pares:
    print(num)
----------------------------------------------------------------------------------------------
- Método IN - dentro
nome = {'Ana', 'Flávia', 'Monique'}

print('Ana' in nome)  # Se for verdadeiro retorna True

if 'Ana' in nome:
    print('Tem uma Ana')
else:
    print('Sumiu.')
----------------------------------------------------------------------------------------------
- Método ADD - adicionar elementos
esportes = {'Fut', 'Vol', 'Nat'}
print(esportes)
esportes.add('Futsal')
print(esportes)
----------------------------------------------------------------------------------------------
- Removendo elementos do conjunto:

Forma 1 - Utilizando Remove() - Apontar o elemento a ser removido
- O remove não retorna o número removido numa variável, ele retorna None
conjunto = {1, 3, 5, 7, 9, 11}
print(conjunto)
conjunto.remove(7)
print(conjunto)

Forma 2 - Discard() - descartar
- O discard também não retorna o número removido e sim None
conjunto = {1, 3, 5, 7, 9, 11}
print(conjunto)
conjunto.discard(5)
print(conjunto)

Forma 3 - Pop() - Nõa necessita de passar parâmetro, ele tira um valor arbitrário
- Retorna o valor que foi removido
conjunto = {1, 3, 5, 7, 9, 11}
print(conjunto)
resultado = conjunto.pop()
print(resultado)

Forma 4 - Clear() - Limpa o conjunto, mas não o apaga
conjunto = {1, 3, 5, 7, 9, 11}
conjunto.clear()
print(conjunto)
----------------------------------------------------------------------------------------------
- Função len() - Retorna o comprimento do conjunto (Número de elementos)
conjunto = {1, 3, 5, 7, 9, 11}
print(len(conjunto))
----------------------------------------------------------------------------------------------
- Função Intersection() - Intersecção de conjuntos - Valores que contídos em ambos os conjuntos
- Retorna um conjunto
notaFabio = {5, 6, 7}
notaClara = {6, 7, 8}
print(notaFabio.intersection(notaClara))

- Também pode ser feito utilizando o e: &
print(notaFabio & notaClara)
----------------------------------------------------------------------------------------------
- União de conjutos - Junta todos os valores de um e outro, formando um novo conjunto
notaFabio = {5, 6, 7}
notaClara = {6, 7, 8}
print(notaClara.union(notaFabio))

- Também pode ser feito utilizando o ou: |
print(notaClara | notaFabio)
----------------------------------------------------------------------------------------------
- Método Difference() - Diferença entre dois conjuntos - Elementos que possuem em apenas um deles
notaFabio = {5, 6, 7}
notaClara = {6, 7, 8}
print(notaClara.difference(notaFabio))

- Também pode ser feito utilizando a subtração: -
print(notaClara - notaFabio)

----------------------------------------------------------------------------------------------
CÓPIAS

Deep Copy - Cada conjunto vai trabalhar separadamente
notaFabio = {5, 6, 7}
notas = notaFabio.copy()
print(notas)
print(notaFabio)
notas.add(9)
print(notas)
print(notaFabio)

Shellow Copy - Os dois conjuntos ficam vinculados
notaFabio = {5, 6, 7}
notas = notaFabio
print(notas)
print(notaFabio)
notas.add(9)
print(notas)
print(notaFabio)
----------------------------------------------------------------------------------------------
- Max, Min e Sum
valores = {1, 6, 2, 8, 3, 7, 11, 25, 88}
print(max(valores))
print(min(valores))
print(sum(valores))
"""
valores = {1, 6, 2, 8, 3, 7, 11, 25, 88}
print(max(valores))
print(min(valores))
print(sum(valores))

