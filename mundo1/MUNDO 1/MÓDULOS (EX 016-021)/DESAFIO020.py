import random

n1 = input('Digite o nome do primeito aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A lista sorteada é:')
print(lista)


