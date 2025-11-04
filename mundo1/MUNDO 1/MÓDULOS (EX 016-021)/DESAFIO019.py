import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
listaalunos = [aluno1, aluno2, aluno3]

print(f'O aluno escolhido foi {random.choice(listaalunos)}')

