"""
Dicionários

Carcterísticas:
1. São apresentados por {}; Listas [] e Tuplas ()
2. Dicionários possuem uma relação chave -> elemento.
3. Dicionários permitem qualquer tipo de dado (inteiro, float, string, ...)
4. Não são ordenados.
5. São utilizados para otimizar a busca de dados, pois basta saber a chave que irá acessar o elemento.

Sobre as chaves:
- Devem ser únicas em cada dicionário.
- Podem ser de qualquer tipo.

Sobre os dados:
- Podem ser duplicados.
- Podem ser de qualquer tipo.
- Se repetir a chave, ele vai pegar o valor do último elemento indicado para aquela chave.

O que é none?
NONE é um dado sem tipo, usado para declarar variáveis que você ainda não sabe o tipo que irá utiizar.
Ex:
dado = None
# -----------------------------------------------------------------------------------------------------
Como declarar? Existem 3 formas:

Forma 1 - Mais usada
Ex:

times_futebol = {'RJ': 'Flamengo', 'SP': 'Corinthians', 'PR': 'Curitiba'}
#  ou
times_futebol = {
    'RJ': 'Flamento',
    'SP': 'Corinthains',
    'PR': 'Curitiba'
}
print(times_futebol)
print(type(times_futebol))

Forma 2 - Utilizando o comando dict()
times_futebol = dict(RJ='Flamengo', SP='Corinthians', PR='Curitiba')
print(times_futebol)
print(type(times_futebol))

Forma 3 - Menos utilizada; fromkeys()
Sintaxe:
variável = {}.fromkeys(iterável, elemento) -> cada item do iterável recebe o mesmo elemento

times_futebol = {}.fromkeys('chave', 'dado')
print(times_futebol)

times_futebol = {}.fromkeys(range(1, 11), 'dado')
print(times_futebol)

# -----------------------------------------------------------------------------------------------------
#  Formas de acessar os elementos do dicionário
# Forma 1
# Se a chave não existir dará erro
times_futebol = {'RJ': 'Flamengo', 'SP': 'Corinthians', 'PR': 'Curitiba'}
print(times_futebol)
print(times_futebol['SP'])

# Forma 2
# Se a chave não existir retornará um elemento do tipo NONE;
times_futebol = {'RJ': 'Flamengo', 'SP': 'Corinthians', 'PR': 'Curitiba'}
print(times_futebol.get('BH'))

times_futebol = {'RJ': 'Flamengo', 'SP': 'Corinthians', 'PR': 'Curitiba'}
print(times_futebol.get('BH', 'Chave não existe')) # Adiciona um valor default para chave inexistente

# Forma 3
# Varifica se a chave apontada existe no dicionário
times_futebol = {'RJ': 'Flamengo', 'SP': 'Corinthians', 'PR': 'Curitiba'}
print('SP' in times_futebol)

# -----------------------------------------------------------------------------------------------------
# Adicionar e alterar elementos no dicionário

# Forma 1 - Mais utilizada
sagas = {
    (1, 2): 'HP',
    (3, 4): 'PJ',
    (5, 6): 'JV'
}

print(sagas)

# Adiciona nova chave com o elemento MR
sagas[(7, 8)] = 'MR'
print(sagas)

# Atualiza a chave (3, 4) com o elemento Digimon
sagas[(3, 4)] = 'Digimon'
print(sagas)

# Forma 2
sagas = {
    (1, 2): 'HP',
    (3, 4): 'PJ',
    (5, 6): 'JV'
}

print(sagas)

# Adiciona nova chave com o elemento MR
dadoNovo = {(7, 8): 'MR'}
print(dadoNovo)

sagas.update(dadoNovo)
print(sagas)

# Para alterar elementos basta utilizar a mesma chave
sagas.update({(3, 4): 'Digimon'})
print(sagas)
# -----------------------------------------------------------------------------------------------------
# Remover valores do dicionário:

# Forma 1 - Função pop()
# Retorna o valor de dentro da chave, podendo usar o elemento posteriormente.
pokemon = {
    'Agua': 'Squirtle',
    'Fogo': 'Charmander',
    'Grama': 'Bulbassauro',
    'Elétrico': 'Pikachu'
}
print(pokemon)

dado = pokemon.pop('Elétrico')
print(pokemon)
print(dado)

# Forma 2 - Usando del -> Não retorna elemento
pokemon = {
    'Agua': 'Squirtle',
    'Fogo': 'Charmander',
    'Grama': 'Bulbassauro',
    'Elétrico': 'Pikachu'
}
print(pokemon)
del pokemon['Elétrico']
print(pokemon)
"""
pokemon = {
    'Agua': 'Squirtle',
    'Fogo': 'Charmander',
    'Grama': 'Bulbassauro',
    'Elétrico': 'Pikachu'
}

print(pokemon)
del pokemon['Elétrico']
print(pokemon)
