"""
Chegou o famoso Dia dos Namorados.
Mateus deixa para decidir o presente em cimada hora.
Ele resolveu comprar um tipo de flor, um presente e escolher um lugar para saírem. Ele anotou todas as opções abaixo:

Flores
Tipo - Preço
Rosas Vermelhas - 145,00
Girassóis - 125,00
Margaridas - 120,00
Flores do campos - 140,00

Presente
Tipo - Preço
Urso de pelúcia - 55,00
Caixa de Bombom - 60,00
Colar - 75,00
Roupas - 40,00

Lugar
Tipo - Preço
Praia - 70,00
Sair para jantar - 150,00
Parque de diversões - 120,00
Hotel - 180,00

— Crie um programa que descubra qual a combinação mais cara, em seguida a mais barata e as opções médias e medianas.
Imprima a combinação em cada caso.
— Use um dicionário para cada item (flor, lugar e presente).
"""
flores = {'Rosas Vermelhas': 145.00, 'Girassól': 125.00, 'Margaridas': 120.00, 'Flores do Campo': 140.00}
presentes = {'Urso de Pelúcia': 55.00, 'Caixa de Bombom': 60.00, 'Colar': 75.00, 'Roupas': 40.00}
lugares = {'Praia': 70.00, 'Sair para jantar': 150.00, 'Parque de Diversões': 120.00, 'Hotel': 180.00}

preco_total = 0
preco_maximo = 0
preco_minimo = 0
aux = 0
flor_cara = ''
presente_caro = ''
lugar_caro = ''
flor_barata = ''
presente_barato = ''
lugar_barato = ''
lista = []

# Combinação mais cara
for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            preco_atual = valor + preco + custo
            lista.append(preco_atual)
            if preco_atual > preco_maximo:
                preco_maximo = preco_atual
                flor_cara = flor
                presente_caro = presente
                lugar_caro = lugar
            if aux == 0:
                preco_minimo = preco_atual
                aux += 1
            else:
                if preco_atual < preco_minimo:
                    preco_minimo = preco_atual
                    flor_barata = flor
                    presente_barato = presente
                    lugar_barato = lugar

print(f'Custo máximo: {preco_maximo} - {flor_cara}, {presente_caro} e {lugar_caro}')
print(f'Custo mínimo: {preco_minimo} - {flor_barata}, {presente_barato} e {lugar_barato}')

lista.sort()
preco_mediano = lista[len(lista) // 2]

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            if valor + preco + custo == preco_mediano:
                print(f'Custo mediano: {preco_mediano} - {flor}, {presente} e {lugar}')

preco_medio = sum(lista) / len(lista)

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            if preco_medio == valor + preco + custo:
                print(f'Custo médio: {preco_medio} - {flor}, {presente} e {lugar}')

print(f'\nMédia total {sum(lista) / len(lista)}')

media_flores = sum(flores.values()) / len(flores)
media_presentes = sum(presentes.values()) / len(presentes)
media_lugares = sum(lugares.values()) / len(lugares)

print(f'\nMédias por categoria:\n'
      f'Flores: {media_flores} / Presentes: {media_presentes} / Lugares: {media_lugares}')
