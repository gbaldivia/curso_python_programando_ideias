"""
Foi realizado uma pesquisa de algumas características e gosts de quatro habitantes incluindo:
- nome
- sexo
- esporte favorito (Natação, Futebol, Vôlei, Tênis)
- idade

Com esses dados faça:
- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
- Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostem de natação chame uma função e
imprima um aviso de que não há homens que gostam de natação.
"""
def pesquisa():
    lista = []
    for i in range(4):
        registros = dict(nome = input('Digite seu nome: '),
                         sexo = input('Digite "F" para Feminino ou "M" para Masculino. Qual seu sexo biológico? '),
                         esporte = input('Ddigite seu esporte favorito entre Natação, Futebol, Vôlei ou Tênis: '),
                         idade = int(input('Digite sua idade: ')))
        lista.append(registros)

    return lista

lista = pesquisa()
cont = 0
soma = 0

def aviso():
    print('Não tem homens que gostam de natação.')

for i in range(4):
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'Natação':
        soma += lista[i]['idade']
        cont += 1

if cont == 0:
    aviso()
else:
    print(f'A média de idade dos homens que gostam de natação é {soma/cont}')
