"""
1 - Crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra para os
preços dos produtos.
Utilizando um loop preencha as listas com 5 produtos e 5 preços, recebendo estes dados do usuário (input).
Por fim, some os preços, imprima o valor toal e os produtos do carrinho.
"""
produtos = []
precos = []
total = float(0)
i = 0
while i < 5:
    produtos.insert(i, input('Insira o nome do produto: '))
    precos.insert(i, float(input('Insira o preço do produto: ')))
    total += precos[i]
    i += 1

i = 0
print('\nVocê tem no seu carrinho: \n')
while i < 5:
    print(f'{produtos[i]} - R$ {precos[i]}')
    i += 1

print(f'Total R$ {total}')
