num = int(input('Digite um numero de 0 a 9999: '))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhar = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidades: {unidades}')
print(f'Dezenas: {dezenas}')
print(f'Centenas: {centenas}')
print(f'Milhar: {milhar}')

