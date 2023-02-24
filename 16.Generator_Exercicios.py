"""
1 — A partir da lista apresentada, criar um Generator contendo apenas animais que comecem com 'C' ou 'A' e que o tamanho
do seu nome seja maior que 5. Por fim, itere e imprima o Generator.

listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha', 'Carneiro', 'Cabra',
'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']
"""
listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha', 'Carneiro', 'Cabra',
                'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

generatorAnimais = (animal for animal in listaAnimais if len(animal) > 5 and (animal[0] == 'A' or animal[0] == 'C'))

for animal in generatorAnimais:
    print(animal, end=' ')
