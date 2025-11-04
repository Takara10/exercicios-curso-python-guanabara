frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A frase {frase} tem {frase.count("A")} letras "A"')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")}')
print(f'A última letra "A" apareceu na posição {frase.rfind("A")}')
