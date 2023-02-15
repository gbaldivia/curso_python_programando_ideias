"""
1 — Criar um sistema de comando de uma loja de jogos.
O programa deve conter pelo menos 6 listas:
1. Indicando quais jogos estão disponíveis para venda
2. Preço dos jogos disponíveis
3. Quantidade de jogos disponíveis na loja
4. Preço de fábrica dos jogos no fornecedor
5. Registro de vendas
6. Registro de compras para o estoque

Todas as informações de um jogo devem estar no mesmo índice em todas as listas.
Crie um menu interativo com as seguintes opções para o usuário:
1. Registrar venda
2. Compra de estoque
3. Resumo da loja
4. Sair
Ao sair indicar que o caixa está fechado.
O utilizador deve ser ápito a controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer
de alterar os valores na lista de quantidades.
"""
jogos = ['The Sims', 'Two Points Campus', 'Two Points Hospital', 'FIFA', 'Tropico 6']
precos = [79.9, 199.99, 119.99, 189.99, 49.99]
disponivel = [15, 8, 4, 21, 5]
preco_fornecedor = [41.5, 150, 73, 121.84, 16.5]
vendas = [0, 0, 0, 0, 0]
compras = [0, 0, 0, 0, 0]

menu = 0

while menu != 4:
    menu = int(input('1 - Registrar venda\n'
                     '2 - Compra de estoque\n'
                     '3 - Resumo da loja\n'
                     '4 - Sair\n'
                     'Digite a opção desejada: '))

    if menu == 1 or menu == 2:
        if menu == 1:
            opcao = 'vender'
        else:
            opcao = 'comprar'
        index = int(input('\n1 - The Sims\n'
                          '2 - Two Points Campus\n'
                          '3 - Two Points Hospital\n'
                          '4 - FIFA\n'
                          '5 - Tropico 6\n'
                          f'Digite o número referente ao jogo que você deseja {opcao}: '))
        quantidade = int(input('Digite a quantidade: '))
        if menu == 1:
            if quantidade <= disponivel[index-1]:
                disponivel[index-1] = disponivel[index-1] - quantidade
                vendas[index-1] = precos[index-1] * quantidade
                print(f'\nVenda de {quantidade} unidades do {jogos[index-1]} realizada!')
            else:
                print(f'\nVenda não realizada, temos apenas {disponivel[index-1]} unidades em estoque.')
        else:
            disponivel[index - 1] = disponivel[index - 1] + quantidade
            compras[index - 1] = preco_fornecedor[index - 1] * quantidade
            print(f'\nCompra de {quantidade} unidades do jogo {jogos[-1]} efetuada!')
    elif menu == 3:
        print('\nRelatório completo:')
        for i, jogo in enumerate(jogos):
            print(f'\n{jogo} - R$ {precos[i]} - Unidades em Loja: {disponivel[i]}')

        print(f'\nTotal de Vendas - {sum(vendas)}')
        for i, jogo in enumerate(jogos):
            print(f'{jogo} - R$ {vendas[i]}')

        print(f'\nRelatório de Compras - {sum(compras)} ')
        for i, jogo in enumerate(jogos):
            print(f'{jogo} - R$ {compras[i]}')

    elif menu == 4:
        print('\nEncerrando o caixa.')

    else:
        print('\nVocê não digitou uma opção válida')
