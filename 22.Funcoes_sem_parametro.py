"""
O que são funções?
- Blocos de código que irão executar uma tarefa específica, podendo ser reutilizada.
- O papel é organizar o código, diminuir o tamanho do programa e facilitar alterações e gerenciamento.
- São declaradas após os comentários iniciais e imports (se houver).
- Exemplos:
1 - print()
2 - input()
3 - type()

Como declarar funções:
def nome_desejado(parametros):
    #Processo

Essa aula será sem parâmetros:
def nome():
    #Processo

# Sempre começar com letrar minúsculas e se for nome composto, separe por underline(_)
# Quando utiliza parênteses, chama a execução da função.
# Sem parênteses chama o abjeto função.

Exemplos:
a)
def teste_frase():
    print('Minha primeira função')

for i in range(0,3):
    teste_frase()

b)
def teste_frase():
    print('Minha primeira função')

frase = teste_frase #Quando crio variáveis do tipo função, deve ser SEM parenteses

print(type(frase))
print(frase()) #É o parenteses que chama a execução da função

# CLASSIFICAÇÃO DE FUNÇÃO
# 1 - Com ou sem retorno
# O retorno serve para retornar uma operação ou variável de dentro da função
# Utiliza a palavra return
# Podemos ter mais de um return na função

Exemplo:
a) Função sem retorno
def operacao():
    contador = 60 # variável local
    contador += 2
    print(f'Contador = {contador}')

print(operacao()) # Retorna None

b) Função com return
# Assim que a função reconhece a palavra return ela finaliza automaticamente

def operacao():
    contador = 60 # variável local
    contador += 2
    print(f'Contador = {contador}')
    return contador

print(operacao()) # Retorna None

2 - Funções recursivas e não recursivas:
O que é recursivo?
- Aquilo que se repete indefinidamente. Uma função recursiva é aquela que retorna a ela mesma.

# Função não recursiva, ou seja, não retorna a ela mesma. É executada apenas uma vez.
# Exemplo
def celsius_to_kelvin():
    celsius = int(input('Digite o valor em Celsius:'))
    kelvin = celsius + 273
    return kelvin

print(celsius_to_kelvin())

# Função RECURSIVA
def celsius_to_kelvin():
    celsius = int(input('Digite o valor em Celsius: '))
    kelvin = celsius + 273
    print(f'Kelvin: {kelvin}')
    sair = input('Deseja sair? ')
    if sair == 'sim':
        return 'Acabou'
    else:
        return celsius_to_kelvin()

print(celsius_to_kelvin())

OBSERVAÇÃO:
# Lembre-se SEMPRE de colocar uma condição de parada na recursividade. Caso contrário cai em um loop infinito.
Vantagem da recursão: torna o código mais limpo e gera sequências mais facilmente.
Desvantagens: a lógica pode ser mais complexa e também usar mais memória.
"""
