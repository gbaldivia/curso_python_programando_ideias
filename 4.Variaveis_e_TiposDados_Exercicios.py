"""
Faça um programa que receba o nome de um aluno e quanto ele tirou na prova.
Imprima em apenas uma linha o nome com o modo title() e quanto a pessoa tirou.

Ex: Carlina tirou 8.
"""

nome = input('Digite o nome do aluno: ')
nota = float(input('Digite a nota do aluno: '))

print(f'{nome.title()} tirou {nota}')
