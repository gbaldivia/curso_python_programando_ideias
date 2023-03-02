"""
Dicionários - Parte 2

Comparação entre Dicionários, Listas e Tuplas:

Quando usar dicinários:
- Conjunto de informações de um mesmo objeto ou pessoa.

Ex:
Funcionários:
Paula, 27 anos, programadora
Gabriel, 30 anos, engenheiro

# Listas:
funcionarios = []
lista1 = ['Paula', 27, 'Engenheira']
lista2 = ['Gabriel', 30, 'Programador']
funcionarios.append(lista1)
funcionarios.append(lista2)
print(funcionarios)
print(funcionarios[0][1])

# Tuplas
tuple1 = ('Paula', 27, 'Engenheira')
tuple2 = ('Gabriel', 30, 'Programador')
funcionario = (tuple1, tuple2)
print(funcionario)
print(funcionario[1][1])

# -----------------------------------------------------------------------------
# Esse é o jeito mais eficaz de encontrar informações
funcionario = {}
dicionario1 = {'nome': 'Paula', 'idade': 27, 'função': 'Engenheira'}
dicionario2 = {'nome': 'Gabriel', 'idade': 30, 'função': 'Programador'}

funcionario['Paula'] = dicionario1
funcionario['Gabriel'] = dicionario2
print(funcionario)
print(funcionario['Paula']['idade'])

# -----------------------------------------------------------------------------
# Como limpar dicionários (Sem excluir o dicionário):

dicionario = {'Programando': 'Ideias'}
print(dicionario)
dicionario.clear()
print(dicionario)
dicionario['Programando'] = ['Ideias']
print(dicionario)

# -----------------------------------------------------------------------------
# Copiando o dicionário
# Deep Copy — Utiliza a função copy()
# Cada dicionário é independente entre si
dicionario = {'Programando': 'Ideias'}
novo = dicionario.copy()
novo['Melhor'] = 'do mundo'
print(dicionario)
print(novo)

# Shallow Copy
# Os dicionários não são independentes entre si
dicionario = {'Programando': 'Ideias'}
novo = dicionario
print(dicionario)
novo['Melhor'] = 'do Mundo'
print(novo)
print(dicionario)
# -----------------------------------------------------------------------------
# Iterar dicionários
personagem = {'Nome': 'Rick', 'Funcao': 'Cientista', 'Neto': 'Morty'}

# Imprime as chaves
for item in personagem:
    print(item)

# Imprime os elementos nas chaves
for item in personagem:
    print(personagem[item])

# -----------------------------------------------------------------------------
# Métodos Keys()
# Retorna uma lista com as chaves do dicionário
personagem = {'Nome': 'Rick', 'Funcao': 'Cientista', 'Neto': 'Morty'}
print(personagem.keys())

# -----------------------------------------------------------------------------
# Método values
# Retorna uma lista com os elementos do dicionário
personagem = {'Nome': 'Rick', 'Funcao': 'Cientista', 'Neto': 'Morty'}
print(personagem.values())

# -----------------------------------------------------------------------------
# Método ítem
# Retorna duplas, sendo as duplas o par chave e elemento
personagem = {'Nome': 'Rick', 'Funcao': 'Cientista', 'Neto': 'Morty'}
print(personagem.items())

for chave, dado in personagem.items():
    print(chave)
    print(dado)

# -----------------------------------------------------------------------------
# Método len():
# Retorna o tamanho do dicionário

# -----------------------------------------------------------------------------
# Max, Min e Sum
# Aceitam apenas dados numéricos. Caso utilize string, irá pegar em ordem alfabética no max e min
dic = {'a': 1, 'b': 2, 'c': 3}
print(max(dic.values()))
print(min(dic.values()))
print(sum(dic.values()))

"""
dic = {'a': 1, 'b': 2, 'c': 3}
print(max(dic.values()))
print(min(dic.values()))
print(sum(dic.values()))
