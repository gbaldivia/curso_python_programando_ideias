"""
1 - A partir da lista apresentada, utilizar List Comprehension para criar outra lista apenas com animais que comece com
a letra 'C' e que o tamanho de seu nome seja menor ou igual a 7.
Por fim imprima a nova lista.

animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe',
'Macaco']

"""
animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe',
           'Macaco']

animais_c = [animal for animal in animais if len(animal) <= 7 and animal[0] == 'C']
print(animais_c)
