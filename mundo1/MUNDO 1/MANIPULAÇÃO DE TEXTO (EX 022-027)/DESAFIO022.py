verde = '\033[32m'
limpa = '\033[0m'
azul = '\033[34m'
amarelo = '\033[33m'
cinza = '\033[36m'
nome = str(input('Digite seu nome: ').strip())
print('Analisando seu nome...')
print (f'Seu nome com letras maiúsculas é {verde}{nome.upper()}{limpa}')
print(f'Seu nome com letras minúsculas é {amarelo}{nome.lower()}{limpa}')
print(f'Seu nome ao todo tem {azul}{len(nome)-nome.count(" ")} letras{limpa}')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {cinza}{len(separa[0])}{limpa} letras.')

