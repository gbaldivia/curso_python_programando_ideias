"""
1 — Faça um programa que contabiliza time de heróis e vilões da seguinte forma:

- Crie um dicionário chamado herói com chave sendo o nome do personagem e o elemento o nível de poder do personagem.
Nível: 1 a 100.
Ex:
heroi = {'Flash':85}

- Crie outro dicionário que serão as armas que podem ser usadas pelo herói, sendo a chave o nome da arma e o elemento o
nível da arma. Sendo o nível de 0 a 100.
Ex:
arma = {'Escudo do Capitão América': 60}

- Crie um último dicionário representando os vilões sendo chave o nome do vilão e no elemento o nível, de 0 a 200.
Ex.
vilao = {'Thanos': 175}

Após isso, o usuário poderá escolher o Herói, uma arma, somar os pontos de poder e escolher um vilão para pular.
Apresente quem foi o vencedor. Caso seja o herói, imprima a arma usada também.
Caso resulte em empate, informa na saída.
"""
heroes = {'Capitão América': 100,
          'Thor': 90,
          'Homem-Aranha': 80,
          'Viuva Negra': 70,
          'Capitã Marvel': 95
          }

armas = {'Escudo do Capitão': 75,
         'Mijonir': 95,
         'Uniforme de aranha': 85,
         'Pistolas e explosivos': 60,
         }

viloes = {'Thanos': 175,
          'Loke': 125,
          'Homem Areia': 115,
          'Hidra': 180,
          'Corvus Glaide': 140
          }

heroi = input('Capitão América\n'
              'Thor\n'
              'Homem-Aranha\n'
              'Viuva Negra\n'
              'Capitã Marvel\n'
              'Escolha o herói: ')

arma = input('\nEscudo do Capitão\n'
             'Mijonir\n'
             'Uniforma de aranha\n'
             'Pistolas e explosivos\n'
             'Escolha uma arma: ')

vilao = input('\nThanos\n'
              'Loke\n'
              'Homem Areia\n'
              'Hidra\n'
              'Corvus Glaide\n'
              'Escolha qual vilão irá enfrentar: ')

poder_heroi = heroes.get(heroi) + armas.get(arma)

if poder_heroi > viloes.get(vilao):
    print(f'{heroi} com a arma {arma} ganhou!')
elif poder_heroi == viloes.get(vilao):
    print(f'\nEmpate entre {heroi} e {vilao}')
else:
    print(f'\n{vilao} venceu.')
