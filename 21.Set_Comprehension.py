"""
Relembrando:

- Não possuem ordenação
- Não possuem elementos repetidos
- São declarados por chaves {}

# Aplicação ---------------------------------------------------------------------------
String - Desordenado e sem letras repetidas
trava_linguas = 'O rato roeu a roupa do rei de roma'
conjunto = {letra for letra in trava_linguas}
print(conjunto)

---------------------------------------------------------------------------------------
Range()

Forma 1:
conjuto_impares = {numero for numero in range(1, 21, 2)}
print(conjuto_impares)

Forma 2:
conjuto_impares = {numero for numero in range(1, 21) if numero % 2 != 0}
print(conjuto_impares)

---------------------------------------------------------------------------------------
# Desafio - Faça usando comprehension de conjuntos, imprimir os múltiplos de 3, porém os não múltiplos devem ser
impressos com a mensagem print('Desconhecido: {numero}')

######### IMPORTANTE - Caso tenha um print dentro do comprehension, será retornado um valor Nona como um dos elementos.

conjuto_impares = {numero if numero % 3 == 0 else print(f'Desconhecido: {numero}') for numero in range(1, 22) }
print(conjuto_impares)

"""
conjuto_impares = {numero if numero % 3 == 0 else print(f'Desconhecido: {numero}') for numero in range(1, 22)}
print(conjuto_impares)
