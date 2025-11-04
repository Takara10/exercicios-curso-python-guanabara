vermelho = '\033[1;31m'
verde = '\033[1;32m'
limpa = '\033[0m'
import random
from time import sleep
print('='* 20)
print('JOGO DA ADIVINHAÇÃO!')
print('='* 20)
num1 = random.randint(0, 5)
num2 = int(input('Digite um número de 0 a 5: '))
sleep(2)
if num1 == num2:
    print(f'{verde}VOCÊ ACERTOU!{limpa}')
else:
    print(f'{vermelho}VOCÊ ERROU!{limpa} Eu pensei no número {verde}{num1}{limpa} e não no {vermelho}{num2}{limpa}!')
    