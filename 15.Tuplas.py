"""
Tuplas

Pareem listas, mas possuem duas diferenças:
1. Não é possível remover e nem adicionar elementos em uma tupla, apenas sobrescrevê-las.
2. Sintaxe: (elemento1, elemento2, elemento3 ...) ou elemento1, elemento2, elemento3 ...

A vírgula é obrigatória!

Vantagens:
1. As Tuplas são mais seguras porque não podemos adicionar ou remover elementos.
2. Processamento é mais rápido.
3. Não há o shallow copy. Tuplas são sempre independentes entre si.

Quano usar uma tupla ao invés de uma lista?
Usar quando não forem necessárias modificações nos dados.
Exemplo: trabalhar com calendário. Os meses e os dias não se alteram.

# ---------------------------------------------------------------------------------------
# Exemplos de declaração de Tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1, )

print(type(tupla1), type(tupla2), type(tupla3), type(tupla4))
# ---------------------------------------------------------------------------------------
# Concatenar duas ou mais tuplas
tuplaNova = tupla1 + tupla5
print(tuplaNova)

# A primeira tupla1 foi apagada e uma nova tupla1 foi criada.
tupla1 = tupla1 + tupla5
print(tupla1)
# ---------------------------------------------------------------------------------------
# Verificar se determinado valor está em uma tupla
print(tupla8)
print(10 in tupla8)
print(False in tupla8)
# ---------------------------------------------------------------------------------------
# Obter a quantidade de vezes que um valor se repete em uma tupla
cores = ('branco', 'azul', 'preto', 'verde', 'amarelo', 'verde')
print(cores.count('verde'))
print(cores.count('amarelo'))
# ---------------------------------------------------------------------------------------
# Acessar elementos em uma tupla
print(tupla8)
print(tupla8[2])
print(tupla8[4])
print(tupla8[-2])
print(tupla8[-4])

for indice in range(0, 3):
    print(f'indice: {indice} - tupla: {tupla6[indice]}')
# ---------------------------------------------------------------------------------------
# Slicing
print(tupla6)
print(tupla6[2:])  # Do indice 2 o final
print(tupla6[2:6])  # Do indice 2 ao 6
print(tupla6[2:7:2])  # Do indice 2 ao 7 pulando 2
# ---------------------------------------------------------------------------------------
# Percorrer tuplas e iterar
# For

for elemento in tupla2:
    print(elemento, end=' ')

total = 0
for elemento in tupla1:
    total += elemento
print(f'\n{total/len(tupla1)}')
print(sum(tupla1))

# While
total = 0
cont = 0
while cont < len(tupla1):
    total += tupla1[cont]
    cont += 1

print(total/cont)
# ---------------------------------------------------------------------------------------
# Obter índice da tupla
cores = ('branco', 'azul', 'preto', 'verde', 'amarelo', 'verde')

for indice, cor in enumerate(cores):
    print(f'Indice: {indice} - Cor: {cor}')

print(cores.index('azul'))
print(cores.index('verde'))  #  Retorna o índice do primeiro valor encontrado
print(cores.index('verde', 4))  # Retorna a partir do índice 4

print(cores.index('verde', 2, 4))  # Busca a palavra verde entre os índices 2 e 4
# ---------------------------------------------------------------------------------------
# Desempacotar tuplas
esporte, meioTrans, pais = tupla5
print(esporte)
print(meioTrans)
print(pais)
# ---------------------------------------------------------------------------------------
# Funções úteis para trabalhar com tuplas
# Apenas para inteiros e floats
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))

# Para obter o tamanho para qualquer tipo de dado
print(len(tupla1))
# ---------------------------------------------------------------------------------------
"""
# Exemplos de declaração de Tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1, )
tupla5 = ('futebol', 'moto', 'França')
tupla6 = ('pizza', True, 18, 5j, 0.43, 'x', True)
tupla7 = tuple(range(11))
tupla8 = tuple(['azul', True, 'x', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])

# Copiar uma tupla
# Não há o efeito shallow copy, porém a declaração é a mesma
tuplaNova = tupla1
print(tupla1)
print(tuplaNova)

tuplaNova = tuplaNova + tupla5
print(tupla1)
print(tuplaNova)
