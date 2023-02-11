"""
Loop for
"""
"""
Loop é utilizado para repetir uma tarefa várias vezes.

O for é uma das ferramentas que realiza esse loop.

Como declarar?

for item in sequencia:
    #processo

Para cada item dentro de uma sequencia faça:
    #processo
    
A sequencia deve ser iterável.
Dados iterável:
- Strings, desmembradas por caracteres. Ex: Filme -> F i l m e
- Listas
- Tuplas
- Dicionários
- Sets (conjuntos)
- Função range
como declarar?
range (número que você quer que comece, número que você deseja que finalize +1)
exemplo:
numero = range(2, 10)
"""
print('-------------------------------- String ------------------------------')
seriado = 'Todo mundo odeia o Chris\n'

for letra in seriado:
    print(letra, end='')

print('-------------------------------- Lista ------------------------------')
numeros = [1, 2, 'oi', True]
for elemento in numeros:
    print(elemento)

print('-------------------------------- Range ------------------------------')
intervalo_num = range(3, 11)
for numero in intervalo_num:
    print(numero, end= ' ')

print('\n-------------------------------- Complemento  Range 1 ------------------------------')
intervalo_num = range(10)
for interv in intervalo_num:
    print(interv, end =' ')

print('\n-------------------------------- Complemento  Range 2 ------------------------------')
intervalo_num = range(3, 19, 3)
for intervalo in intervalo_num:
    print(intervalo, end=' ')

print('\n-------------------------------- Complemento  Range 3 ------------------------------')
intervalo_num = range(18, 4, -2)
for intervalo in intervalo_num:
    print(intervalo, end=' ')

print('\n-------------------------------- Condicional em Loop ------------------------------')
num = range(2, 20)
for numero in num:
    if numero % 2 == 0:
        print(f'Achei um número par, número: {numero}')

print('\n-------------------------------- For consecutivo ------------------------------')
fruta = 'abacate'
valor = range(1, 2)

for letra in fruta:
    if letra == 'a':
        for num in valor:
            print('Achei a letra a')

print('\n-------------------------------- For com IF ------------------------------')
string = 'abcdefghijklmnopqrstuvwxyz'
for letra in string:
    print(letra, end='/')
    if letra == 'g':
        break

print('\n-------------------------------- Enumerate ------------------------------')
heroi = 'Batman'

for valor in enumerate(heroi):
    print(valor)
