"""
Para cada número par em um grupo de 1 a 9, adicione esse número elevado ao quadrado no conjunto, se o número for ímpar
adicione 2 elementos, 1 por vez: 'Sou', 'Ímpar'. Qual foi a resposta?
Porque 'Sou', 'Ímpar' só apareceu uma vez?
Resposta: Conjuntos não aceitam conjuntos repetidos.
"""
itens = set()
impares = {numero ** 2 if numero % 2 == 0 else 'Sou' if num == 0 else 'Ímpar' for num in range(0, 2) for numero in range(1, 10)}
print(impares)

